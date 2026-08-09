// demo.ts —— 用 Node 直接运行（类型会被"擦掉"）
interface TextContent {
  type: "text";
  text: string;
}

function describe(c: TextContent): string {
  return `[${c.type}] ${c.text}`;
}

// 注意：没有任何 new、没有任何类
const msg = { type: "text", text: "你好" };
console.log(describe(msg));

// 关键：下面这行如果取消注释会【直接报错】——
// "TextContent" 只被用作类型，但运行时不存在这个东西
// console.log(msg instanceof TextContent);

console.log("运行时 msg 的真实面目:", JSON.stringify(msg));
console.log("typeof msg =", typeof msg); // 就是 "object"，仅此而已
