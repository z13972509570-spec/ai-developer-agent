"""开发 Agent"""
import logging
from typing import Dict, List
from .planner import TaskPlanner
from .executor import ToolExecutor


class DeveloperAgent:
    """AI 开发 Agent"""
    
    def __init__(self):
        self.planner = TaskPlanner()
        self.executor = ToolExecutor()
        self.logger = logging.getLogger(__name__)
    
    def run(self, task: str) -> Dict:
        """运行任务"""
        self.logger.info(f"开始处理任务: {task}")
        
        # 1. 理解任务
        plan = self.planner.create_plan(task)
        
        # 2. 执行步骤
        results = []
        for step in plan["steps"]:
            result = self.executor.execute(step)
            results.append(result)
            
            # 3. 验证结果
            if not result.get("success"):
                self.logger.warning(f"步骤失败: {step}")
        
        return {
            "task": task,
            "plan": plan,
            "results": results,
            "status": "completed" if results else "failed",
        }
    
    def execute_file(self, path: str, action: str) -> Dict:
        """操作文件"""
        return self.executor.execute_file(path, action)
