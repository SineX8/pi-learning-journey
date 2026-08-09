# Mission: 成为能设计并交付 agent 产品的技术音频工程师

## Why
用户是服务游戏音效设计师的技术音频（technical audio），负责开发提效工具。他判断 AI agent 是下一代音频工具的形态，需要能独立设计、实现、评估 agent 产品，而不是只会调用现成框架。

## Success looks like
- 能设计一个 agent 产品的架构（事件驱动核心 + 可替换 UI 壳），并讲清每个设计决策的代价
- 能用 TS + Electron 独立实现一个面向音效设计师的 agent 工具（如批量素材分析/处理 agent）
- 能为自己的 agent 搭建评估体系（确定性测试 harness + 真实任务基准）
- 读懂 pi 源码后，能把其模式（事件流、harness、provider 抽象、扩展点）迁移到自己的产品

## Constraints
- 精通 Python；TypeScript 从零开始（第 1 课已完成基础词汇）
- 异步编程零基础（第 2 课按零基础重写）
- 业余时间学习；偏好"读真实源码 + 可运行实验"而非理论教程
- 教学语言：中文；示例领域：游戏音频（素材、响度/LUFS、DAW、批处理）

## Out of scope
- langchain 框架内部（目标由 pi 的 provider 抽象覆盖后按需再看）
- Python 生态对照（用户已跨越对照阶段，要求直接教 TS 机制）
- Web Audio API 深入（只在单位坑等必要处提及）
