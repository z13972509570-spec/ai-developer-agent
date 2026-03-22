"""任务规划器"""
import re
from typing import Dict, List


class TaskPlanner:
    """任务规划器"""
    
    def __init__(self):
        self.action_patterns = {
            "create_file": ["创建", "新建", "添加", "create"],
            "edit_file": ["修改", "编辑", "更新", "edit"],
            "delete_file": ["删除", "remove"],
            "run_command": ["运行", "执行", "run"],
            "read_file": ["读取", "查看", "read"],
        }
    
    def create_plan(self, task: str) -> Dict:
        """创建执行计划"""
        steps = []
        
        # 分解任务为步骤
        keywords = task.lower()
        
        if "创建" in task or "新建" in task or "create" in keywords:
            steps.append({"action": "create_file", "description": "创建文件"})
        
        if "运行" in task or "执行" in task or "run" in keywords:
            steps.append({"action": "run_command", "description": "运行命令"})
        
        if "测试" in task or "test" in keywords:
            steps.append({"action": "run_command", "description": "运行测试"})
        
        if not steps:
            steps.append({"action": "analyze", "description": "分析任务"})
        
        return {
            "task": task,
            "steps": steps,
            "estimated_time": len(steps) * 5,
        }
