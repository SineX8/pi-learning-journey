"""asyncio 关键事实完整演示（对应第 13 节⑥）。
运行：python3 asyncio_facts.py
每一段输出都对应一条事实，总耗时约 3 秒。
"""
import asyncio
import time

start = time.monotonic()


def elapsed() -> str:
    return f"{time.monotonic() - start:5.2f}s"


# ---------- 基础：async def 定义的是"协程函数" ----------
async def download(name: str, seconds: float) -> str:
    """模拟下载：等待 seconds 秒后返回文件名。await 点 = 让出控制权。"""
    print(f"  [{elapsed()}] {name} 开始下载")
    await asyncio.sleep(seconds)  # 模拟 I/O 等待；在这里让出事件循环
    print(f"  [{elapsed()}] {name} 下载完成")
    return name


def demo_facts_1_2():
    """这是一个普通同步函数——注意它里面不能出现 await（事实 5）。"""
    print("== 事实 1+2：调用 async 函数不会执行，只造出 coroutine 对象 ==")
    coro = download("ghost.wav", 1)
    print(f"  调用后得到：{coro!r}")
    print("  注意：没有任何'开始下载'的打印——函数体一行都没跑！")
    print("  coroutine 必须被 await / gather / asyncio.run 驱动才会执行（见 main）")
    coro.close()  # 演示用：关闭未被驱动的 coroutine，避免 RuntimeWarning


async def main():
    # ---------- 事实 2 续：await 驱动 coroutine 执行到底 ----------
    print("== 事实 2：await 驱动 coroutine 执行到底 ==")
    result = await download("kick.wav", 0.5)
    print(f"  [{elapsed()}] await 拿到返回值：{result!r}")

    # ---------- 事实 4：gather 并发 ----------
    print("== 事实 4：gather 并发——总耗时 ≈ 最慢的一个（0.8s），不是总和 ==")
    t0 = time.monotonic()
    results = await asyncio.gather(
        download("a.wav", 0.8),
        download("b.wav", 0.3),
        download("c.wav", 0.5),
    )
    print(f"  [{elapsed()}] 全部完成：{results}")
    print(f"  本段耗时 {time.monotonic() - t0:.2f}s ≈ 0.8s（等待时间重叠了）")
    print("  观察'完成'的顺序：按耗时先后（b→c→a），不是启动顺序——并发的直接证据")

    # ---------- 对照：串行 await ----------
    print("== 对照：for 循环里逐个 await = 串行，耗时相加 ≈ 1.6s ==")
    t0 = time.monotonic()
    for name, s in [("a.wav", 0.8), ("b.wav", 0.3), ("c.wav", 0.5)]:
        await download(name, s)
    print(f"  本段耗时 {time.monotonic() - t0:.2f}s ≈ 0.8+0.3+0.5")


# ---------- 事实 3：asyncio.run 是同步世界进入异步世界的唯一入口 ----------
if __name__ == "__main__":
    demo_facts_1_2()      # 同步函数，直接调
    asyncio.run(main())   # 启动事件循环，跑 main 直到结束

    # ---------- 事实 5（最大坑）：sync 函数里没法直接 await ----------
    # 取消下面两行的注释会直接 SyntaxError——await 只能出现在 async 函数里：
    #
    # def sync_fn():
    #     await download("x.wav", 1)
    #
    # 而同步函数里想"运行"一个 coroutine，也只能回到 asyncio.run：
    # asyncio.run(download("x.wav", 1))   # 每个 asyncio.run 都是一次独立的事件循环
