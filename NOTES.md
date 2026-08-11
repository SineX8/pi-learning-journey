# 教学偏好与工作笔记

## 用户偏好（必须遵守）

- 先答问题再动手；直接、技术向、无客套
- 对熟悉领域可以用 Python 类比锚定；**对异步编程用户明确要求不再对照 Python，直接教 TS 机制**
- 不熟悉的主题要"从零、够详细"，不要跳步；熟悉的主题挑重点讲
- 示例优先：pi 真实源码（标注文件路径）> 音频领域自编例 > 抽象例
- 好问题的答案精简后回收到网页对应章节（"Q&A 实录"模式）
- 网页改动后必须验证：提取 `<script>` 跑 `node --check`（模板字符串里的反引号/`${}` 曾两次搞崩整页）

## Playground 维护教训

- 高亮层与 textarea 字体度量必须完全一致（全局 code 样式曾致光标漂移）
- 程序滚动后两层滚动位置都要同步
- 输出已改流式渲染（主函数结束后的迟到 log 也要可见——用户曾因此困惑心跳消失）
- 正则写进 keydown 逻辑前先在 node 里模拟验证（\n 转义栽过两次）

## 网站架构要点

- 章节 id（data-section）是进度键，重排/重写必须保留
- TOC、scroll spy、hash 路由、完成状态全部由 id 自动派生，新增章节零配置
- pre[data-playground] 自动出现"试一试"；ASCII 图加 data-lang="text"
- 每节末尾有测验卡（QUIZZES 数据，纯概念题、不考 pi 源码），全部答对才解锁"标记完成"按钮；通过状态存 state.quiz。新增章节时必须配 2-4 道题；选项注意长度相近、答案位置打散、配解析（retrieval practice + 即时反馈）

## 部署工作流（用户明确要求 2026-08-11）

- 用户从飞书发消息让改网站时：**改完直接 commit + push + 用 ship-static-site skill 验证线上**，不要先问。用户在手机端看 GitHub Pages（https://sinex8.github.io/pi-learning-journey/），不推看不到
- 本地服务器未必在跑：`./serve.sh` 起 localhost:8080；验证线上走代理 `--proxy=http://127.0.0.1:7892`
- Pages 构建卡 building 时手动触发 `POST /pages/builds`（用 git credential fill 的 token）

## 课程模板（用户要求 2026-08-11，/teach）

第 3 课起，凡涉及 pi 源码的课程必须包含三段结构：
1. **文件结构与代码入口**：源文件位置地图（目录树代码块）+ 入口函数 + 建议读码路线
2. **代码架构与核心机制讲解**：正文主体
3. **作业**：读码题 / 动手题 选一

已落地：l1-s1（第 3 课）、lp-0（第 4 课）。后续 lesson-harness/product/evals 照此模板。
