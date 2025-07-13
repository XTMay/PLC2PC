# PLC→PC Control System Transition Course (20 × 50 mins)

> 🎯 **Course Goals**  
> - Understand PLC-to-PC hybrid control architecture  
> - Learn Python & Object-Oriented Programming (OOP)  
> - Build backend APIs and integrate with databases  
> - Create a frontend control panel with real-time feedback  
> - Communicate with devices using Modbus protocol  

---

## 📘 Course Roadmap

| Week | Lesson | Topic | Key Concepts | Practice / Assignment |
|------|--------|-------|--------------|------------------------|
| 1 | Lesson 01 | Python Basics + Environment Setup | Python syntax, variables, types, I/O; Anaconda / Jupyter / VS Code | Run `print("Hello PLC")`; card game logic |
| 1 | Lesson 02 | Control Flow, Functions, Modules | `if`, `for`, `while`; function definitions; pip; module creation | Factorial calculator / installable utility module |
| 2 | Lesson 03 | OOP I – Classes & Objects | Class, attribute, method, `__init__` | `Dog` class + live coding |
| 2 | Lesson 04 | OOP II – Encapsulation & Composition | Object composition, private members | CLI: 3-color lamp controller (HW ①) |
| 3 | Lesson 05 | OOP III – Inheritance & Polymorphism | Inheritance, method overriding, ABCs | Extend base `Sensor` to `TempSensor` |
| 3 | Lesson 06 | File I/O & Logging | File read/write (JSON/CSV), `logging` | Save and log lamp state |
| 4 | Lesson 07 | System Design Thinking | Layered control system, modularity | Draw PLC→PC system layers |
| 4 | Lesson 08 | Sync/Async, Concurrency & Parallelism | Blocking vs non-blocking, `asyncio`, `threading` | Async lamp blinking example |
| 5 | Lesson 09 | Serial Communication Basics | RS-232/485, `pyserial` | Read virtual serial input |
| 5 | Lesson 10 | Modbus Protocol I | Function codes 01/03/05/06, `pymodbus` TCP | Read/write simulated Modbus registers (HW ②) |
| 6 | Lesson 11 | Modbus Protocol II – Device Drivers | Encapsulate device control in class | `ModbusLampDriver.toggle()` |
| 6 | Lesson 12 | RESTful API with FastAPI | HTTP verbs, routes, Pydantic | Build `/api/lamps` endpoints |
| 7 | Lesson 13 | Database + ORM Basics | SQLite, SQLModel, CRUD | Persist `LampState` to database |
| 7 | Lesson 14 | SQL in Practice | SELECT/INSERT/UPDATE/DELETE, indexing | Stats & history queries |
| 8 | Lesson 15 | API × DB Integration | Transactions, pagination, DI | Toggle lamp → save to DB → return JSON |
| 8 | Lesson 16 | Frontend Basics (HTML/CSS/JS) | Tags, layout, fetch API | Button UI to toggle lamps |
| 9 | Lesson 17 | React Quickstart | State, props, hooks, Vite | Interactive LED control panel (HW ③) |
| 9 | Lesson 18 | WebSocket & Realtime Updates | FastAPI WS, React updates | Live Modbus value chart |
| 10 | Lesson 19 | Docker & Deployment | Dockerfile, Compose, service packaging | Fullstack deployment (backend + frontend) |
| 10 | Lesson 20 | Capstone Demo & Future Paths | Project presentations, cloud/edge tools | Team demo + career advice |

---

## 🎓 Learning Milestones

1. **Lessons 1–4**: Python + OOP foundations → CLI tools & object modeling  
2. **Lessons 5–8**: System architecture, async concepts, logging  
3. **Lessons 9–11**: Serial + Modbus communication, driver abstraction  
4. **Lessons 12–15**: Backend APIs, DB, real-world backend  
5. **Lessons 16–20**: Fullstack frontend + deployment + capstone

---

## ✅ Evaluation

| Component | Weight |
|----------|--------|
| GitHub Repos | Required per stage |
| Quizzes | 30% |
| Assignments (CLI/Modbus/Web) | 30% (10% each) |
| Final Capstone Demo | 30% |
| Participation | 10% |

---

## 🧰 Tools & Resources

- [Python Crash Course (中文)]  
- [FastAPI Documentation](https://fastapi.tiangolo.com/)  
- [React Docs](https://react.dev/)  
- [ModSim / QModMaster / pymodbus]  
- Optional: PLC lab kits or I/O simulators

---

## 📅 Schedule

- 🕒 1 live 50 mins lesson/week
- ⌨️ 3–5 hours weekly practice recommended
- 👨‍🏫 Ongoing support from instructor via email
---

## 📝 How to Register

📩 Email: may200852@gmail.com 
💬 LINE/WeChat available upon request  
🧪 Free trial lesson available!

---

> 💬 Questions? Discuss via GitHub Issues or class group chat. Let’s build, control, and grow!
---

# 🧭 从 PLC 到 PC 控制系统开发 – 20节课实战课程介绍（简体中文）

🚀 用 Python + FastAPI + Vue + SQL + Modbus，10 周带你从 PLC 工程师转型为现代控制系统开发者！

---

## 🎯 课程目标

- 建立从 PLC 到 PC 控制架构的完整理解
- 掌握前后端协作、API 通信与数据库整合技巧
- 实作网页控制界面、后端逻辑、数据记录系统
- 学习并应用 Modbus 通信控制装置

---
> **对象**：拥有 PLC 基础、无 Python 经验的工程师 / 学员。
>
> **结课能力**：
>
> 1. **完整理解** PLC-PC 混合控制架构
> 2. **熟练** 使用 Python\&OOP 进行设备建模与业务逻辑编写
> 3. **掌握** 前后端协作、API 通信、数据库整合
> 4. **实作** 网页控制 UI、后端逻辑、数据记录系统
> 5. **应用** Modbus 协议控制真实/模拟装置

---

## 课程路线图

| 周次 | 课次        | 主题                    | 关键知识点                                                                     | 实战练习 / 作业                                     |
| -- | --------- | --------------------- | ------------------------------------------------------------------------- | --------------------------------------------- |
| 1  | Lesson 01 | Python 入门 + 环境搭建      | PLC vs PC 架构；Python 基本语法、变量、数据类型、运算符、输入输出；Anaconda / VS Code / Jupyter 安装 | 安装 Python3.12 并运行 `print("Hello PLC")`；扑克牌小游戏 |
| 1  | Lesson 02 | 控制流、函数、模块与 pip        | if/for/while；函数定义、返回值、Docstring；模块导入与 pip 库管理                             | 计算阶乘 / 编写工具模块并安装使用                            |
| 2  | Lesson 03 | **OOP 基础 I**：类、对象     | Attribute / Method；实例化；`__init__`                                         | **Dog 类**\&bark 示例；课堂 live coding             |
| 2  | Lesson 04 | **OOP 基础 II**：封装 & 组合 | 私有属性；组合、聚合；`Lamp` + `LampGroup`                                           | 三色灯 CLI 控制器(作业①)                              |
| 3  | Lesson 05 | **OOP 进阶**：继承 & 多态    | 继承层次；方法重写；抽象基类                                                            | `Sensor` 基类 → `TempSensor`,`PressureSensor`   |
| 3  | Lesson 06 | 文件与日志                 | 文件读写(JSON/CSV)；logging 模块                                                 | 把灯切换记录写 JSON/log 文件                           |
| 4  | Lesson 07 | 系统设计思维                | 控制系统分层架构（I/O、驱动、逻辑、接口）；模块解耦与协作                                            | 绘制三层 PLC-PC 控制系统架构图                           |
| 4  | Lesson 08 | 同步 / 异步 / 并发 / 并行     | 阻塞 vs 非阻塞；`threading`、`asyncio`、调度策略                                      | 用 asyncio 控制并发灯闪烁                             |
| 5  | Lesson 09 | 串口通信基础                | RS-232/485 概念；`pyserial` 读写                                               | 用 USB-TTL 模拟器读虚拟串口数据                          |
| 5  | Lesson 10 | **Modbus 协议 I**       | 功能码 01/03/05/06；`pymodbus` TCP 客户端                                        | 读写模拟 Modbus 寄存器(作业②)                          |
| 6  | Lesson 11 | **Modbus 协议 II**：驱动封装 | 设备驱动类设计；异常处理；重试逻辑                                                         | `ModbusLampDriver.toggle()` 实现                |
| 6  | Lesson 12 | RESTful API 基础        | HTTP 方法；FastAPI 路由；Pydantic                                               | 构建 `/api/lamps` GET/POST                      |
| 7  | Lesson 13 | 数据库基础 & ORM           | SQLite / PostgreSQL；SQLModel CRUD                                         | 创建 `LampState` 表并持久化                          |
| 7  | Lesson 14 | SQL 实战                | 基本语句（SELECT/INSERT/UPDATE/DELETE）；索引、查询优化                                 | 编写 SQL 查询控制记录与统计分析                            |
| 8  | Lesson 15 | API × DB 整合           | 依赖注入；事务；分页查询                                                              | POST 切换灯 → 写 DB → 返回 JSON                     |
| 8  | Lesson 16 | 前端零基础 HTML/CSS/JS     | 语义标签；Flex 布局；fetch API                                                    | 静态页面按钮控制灯状态                                   |
| 9  | Lesson 17 | React 快速入门            | 组件、状态、props；Vite                                                          | LED 控制面板 Demo(作业③)                            |
| 9  | Lesson 18 | WebSocket 与实时推送       | FastAPI WebSocket；React hook                                              | 实时显示寄存器值折线图                                   |
| 10 | Lesson 19 | 部署：Docker & Compose   | Dockerfile、compose.yml；端口映射                                               | 打包 API + React + 模拟器全栈镜像                      |
| 10 | Lesson 20 | Capstone Demo & 未来拓展  | 学员项目演示；OPC UA、Grafana、Cloud Edge                                          | 课堂答辩 + 个人成长路径建议                               |

---

## 各阶段学习成果

1. **第 1–4 课**：Python 基础语法 & OOP 思维 → 能写 CLI 小工具。
2. **第 5–8 课**：系统结构 + 异步概念 + 日志处理能力。
3. **第 9–11 课**：掌握 Modbus 通信并封装为驱动类。
4. **第 12–15 课**：后端 API × 数据库 × Web 前端实时控制与监测。
5. **第 16–20 课**：Docker 一键部署、自动化测试、Capstone 全栈演示。

---

## 评估方式

* 📁 **代码仓库**：每阶段 push GitHub，老师提交 PR Review
* ✅ **单元测验**：课后小测验 (Quizizz) 30%
* 🛠 **阶段项目**：三色灯 CLI / Modbus 驱动 / Web Panel，各 10%
* 🌟 **Capstone**：综合项目演示 30%

---

## 🧪 实作亮点

- 控制设备开/关（模拟 LED/马达）
- API 接口开发 + Swagger 调试
- Web 页面状态同步与按钮操作
- 写入设备历史记录到数据库
- 模拟温度读取、设备联动控制

---

## 📬 报名方式

📩 邮箱联系：may200852@gmail.com 
💬 可提供免费试听课、技术咨询、环境安装协助

---

> 本课程适合希望将控制能力提升为「现代软件开发能力」的从业者  
> 完全为工业背景人士量身打造，无需资工基础！

---

⭐ 如果你准备好将你的控制逻辑能力延伸到软件世界，欢迎加入我们！
