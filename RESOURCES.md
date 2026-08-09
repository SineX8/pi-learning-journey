# Agent 学习 Resources

## Knowledge

- [TypeScript 入门教程 — xcatliu](https://ts.xcatliu.com/introduction/index.html)
  中文、语法覆盖全、例子密。Use for: TS 语法案头查询，第 1 课配套参考。
- [TypeScript 官方 Handbook](https://www.typescriptlang.org/docs/handbook/intro.html)
  权威语义定义。Use for: narrowing、declaration merging 等细节的第一出处。
- [MDN: JavaScript 并发模型与事件循环](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Execution_model)
  事件循环官方展开版。Use for: 第 2 课 §3 的 primary source。
- [MDN: Promise](https://developer.mozilla.org/zh-CN/docs/Web/JavaScript/Reference/Global_Objects/Promise)
  组合器完整语义与边界行为。Use for: 第 2 课 §2 的 primary source。
- [Rob Pike: Concurrency Is Not Parallelism](https://go.dev/talks/2012/waza.slide)
  经典演讲幻灯片。Use for: 并发 vs 并行的权威区分。
- [Node.js: TypeScript 类型擦除模式](https://nodejs.org/api/typescript.html)
  erasable syntax 规则出处。Use for: 理解 pi 仓库的 TS 写法约束。
- [TypeScript Deep Dive — basarat](https://basarat.gitbook.io/typescript/)
  进阶坑与最佳实践。Use for: 第 1 课之后的深入阅读。
- pi 源码本身（`packages/ai/src/types.ts`、`packages/agent/src/agent-loop.ts`）
  活教材。Use for: 全部课程的代码语境。

## Wisdom (Communities)

- pi 仓库的 GitHub Issues/Discussions（agent 工程实践的一手讨论）
- 待补充：高质量 TS/音频技术社区（用户暂未表达加入意愿，不主动推）

## Gaps

- 面向零基础的中文 JS 异步图解资源（目前靠自研课程 + MDN 补齐）
- agent harness engineering 的系统化外部资料（目前以 pi 源码为唯一教材）
