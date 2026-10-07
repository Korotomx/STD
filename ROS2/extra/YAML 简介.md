---
tags:
  - YAML
  - 参考Reference
---

# YAML 简介：不只是 ROS2 参数

**时间:** 2026-10-07
**标签:** #YAML #参考Reference

## 本质

YAML 是通用的「数据序列化格式」——把结构化数据（键值对 / 列表 / 嵌套）写成一段**人和机器都能读**的文本，和 JSON / XML / TOML 是同类。

ROS2 只是借用它来写参数。**参数文件是 YAML 的一个应用场景，不是 YAML 的全部。**

## 在 ROS2 里的应用

- 参数文件 `params.yaml`（见 [[N033 YAML参数文件与配置分离]]）
- launch 文件（ROS2 支持 Python / XML / YAML 三种写法，Python 最常见）
- RViz 配置 `.rviz`（本质是 YAML）
- MoveIt / Nav2 等上层生态的配置

## 在 ROS2 之外

| 场景 | 文件 |
| ---- | ---- |
| Docker Compose（描述服务怎么起） | `docker-compose.yml` |
| Kubernetes（描述应用部署） | `*.yaml` |
| CI/CD 流水线 | `.github/workflows/*.yml`、`.gitlab-ci.yml` |
| Ansible（自动化剧本） | `playbook.yml` |

两个 mini 例子（格式你已经会认了）：

```yaml
# Docker Compose
services:
  web:
    image: nginx:latest
    ports:
      - "8080:80"
```

```yaml
# Kubernetes
apiVersion: apps/v1
kind: Deployment
spec:
  replicas: 3
  template:
    spec:
      containers:
        - name: app
          image: myapp:v1
```

核心思想都一样：**用人类友好的文本，描述一份机器要照着执行的结构化配置。**

## 为什么流行

1. **可读性好**：缩进嵌套，没有 JSON 那种满屏 `{ } "`
2. **支持注释**（`#`）：JSON 不支持，配置场景这很关键
3. **人机通吃**：人好写、机器好解析

## 通用坑（不是 ROS2 专属）

- **缩进敏感**——层级靠空格对齐，错一个空格层级就错
- **类型靠字面量推断**——`30` 是数字、`"30"` 是字符串
- **布尔陷阱**——`yes/no/on/off` 被当布尔值（YAML 1.1 经典坑，Docker 也栽过）

## 相关

[[N033 YAML参数文件与配置分离]]
