class Solution:
    def isValid(self, s: str) -> bool:
        # Initialize an empty list to be used as a stack
        stack = []

        # Loop through each character in the input string
        for i in range(len(s)):

            # Check if the character is an opening bracket
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                # Push opening bracket onto the stack
                stack.append(s[i])

            else:
                # If a closing bracket is found but stack is empty, it's invalid
                if len(stack) == 0:
                    return False

                # Match current closing bracket with the top of the stack
                if (stack[-1] == '(' and s[i] == ')') or \
                   (stack[-1] == '{' and s[i] == '}') or \
                   (stack[-1] == '[' and s[i] == ']'):
                    # If matched, pop the top element from the stack
                    stack.pop()
                else:
                    # If not matched, it's invalid
                    return False

        # After processing all characters, the stack should be empty if valid
        return len(stack) == 0


# 👇 User interaction and testing
if __name__ == "__main__":
    # Prompt user to input a string with brackets
    user_input = input("🔎 Enter a string containing brackets to validate: ")

    # Create an instance of the Solution class
    sol = Solution()

    # Call the isValid method and print result
    if sol.isValid(user_input):
        print("✅ The input string is VALID!")
    else:
        print("❌ The input string is NOT valid.")
