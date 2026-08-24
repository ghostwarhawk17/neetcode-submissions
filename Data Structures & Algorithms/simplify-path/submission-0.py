class Solution:
    def simplifyPath(self, path: str) -> str:
        path1 = path.split("/")
        stack = []
        for part in path1:
            if part == "" or part == ".":
                continue
            if part == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(part)
        return "/"+ "/".join(stack)
