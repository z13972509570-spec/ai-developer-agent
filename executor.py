"""工具执行器"""
import subprocess
import logging
from pathlib import Path
from typing import Dict


class ToolExecutor:
    """工具执行器"""
    
    def __init__(self):
        self.logger = logging.getLogger(__name__)
    
    def execute(self, step: Dict) -> Dict:
        """执行步骤"""
        action = step.get("action")
        
        if action == "create_file":
            return self.execute_file("temp.py", "create")
        elif action == "run_command":
            return self.run_command("echo 'done'")
        elif action == "analyze":
            return {"success": True, "result": "分析完成"}
        
        return {"success": False, "error": "Unknown action"}
    
    def execute_file(self, path: str, action: str) -> Dict:
        """操作文件"""
        try:
            p = Path(path)
            if action == "create":
                p.parent.mkdir(parents=True, exist_ok=True)
                p.write_text("# Created by AI Developer Agent\n")
                return {"success": True, "path": path}
            elif action == "read":
                content = p.read_text() if p.exists() else ""
                return {"success": True, "content": content}
            return {"success": False, "error": "Unknown action"}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def run_command(self, cmd: str) -> Dict:
        """运行命令"""
        try:
            result = subprocess.run(
                cmd, shell=True, capture_output=True, timeout=30
            )
            return {
                "success": result.returncode == 0,
                "stdout": result.stdout.decode(),
                "stderr": result.stderr.decode(),
            }
        except Exception as e:
            return {"success": False, "error": str(e)}
