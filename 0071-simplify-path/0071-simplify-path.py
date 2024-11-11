class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        segments = path.split('/')
        stack = []

        for segment in segments:
            # Ignore '.' or empty segments
            if segment == '' or segment == '.':
                continue
            # Go up one directory if '..' and the stack is not empty
            elif segment == '..':
                if stack:
                    stack.pop()
            # Otherwise, push the directory name to the stack
            else:
                stack.append(segment)

        # Join the stack to form the simplified canonical path
        return '/' + '/'.join(stack)
        