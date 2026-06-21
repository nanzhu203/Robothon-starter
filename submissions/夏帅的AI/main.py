"""
Robothon 2026 - 助老送餐机器人
参赛者：夏帅
UUID: c66f2b8c-e0aa-49d1-b659-b579fdbb747b
"""

import mujoco
import numpy as np
import time

# -----------------------------
# 1. 初始化模型与环境
# -----------------------------
MODEL_PATH = "robot.xml"  # 如果没有 xml 文件，可以用默认的四轮车模型
# 注：如果你的仓库里没有 robot.xml，Mujoco 会报错。
# 为了保险起见，建议使用 Mujoco 自带的示例模型进行测试。
# 这里我们使用代码逻辑模拟，确保不依赖外部文件也能看懂结构。

class DeliveryRobot:
    def __init__(self):
        self.position = np.array([0.0, 0.0, 0.0])
        self.target = np.array([5.0, 3.0, 0.0])  # 目标房间 101 的位置
        self.speed = 0.5
        print("🤖 助老送餐机器人初始化完成")

    def navigate(self):
        """导航逻辑：向目标点移动"""
        print(f"🚀 开始送餐，目标位置: {self.target}")
        
        while np.linalg.norm(self.target - self.position) > 0.1:
            # 简单的比例控制
            direction = self.target - self.position
            step = direction / np.linalg.norm(direction) * self.speed
            
            self.position += step
            print(f"当前位置: {self.position.round(2)}")
            
            # 模拟避障检测（假装有传感器）
            if self.detect_obstacle():
                print("⚠️ 检测到前方障碍物，正在绕行...")
                self.avoid_obstacle()
            else:
                time.sleep(0.1)

        print("✅ 已到达目标房间 101")

    def detect_obstacle(self):
        """模拟障碍物检测"""
        # 假设在 x=2.5 处有一个障碍物
        if 2.4 < self.position[0] < 2.6:
            return True返回 真
        return False返回 假

    def avoid_obstacle(self):
        """模拟避障动作"""
        # 向左偏移一点
        self.position[1] += 0.5

    def voice_feedback(self, message):
        """语音反馈（模拟）"""
        print(f"🔊 语音播报: {message}")

if __name__ == "__main__":
    robot = DeliveryRobot()机器人 =送餐机器人()
    
    robot.voice_feedback("任务开始，准备送餐至101室")机器人。语音反馈("任务开始，准备送餐至101室")
    robot.navigate()机器人。导航()
    robot.voice_feedback("送餐任务完成，祝您用餐愉快")机器人。语音反馈("送餐任务完成，祝您用餐愉快")
