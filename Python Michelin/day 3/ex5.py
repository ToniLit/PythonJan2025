# def draw_rectangle(width, height):
#     for i in range(height):
#         if i == 0 or i == height - 1:
#             print('#' * width)
#         else:
#             print('#' + ' ' * (width - 2) + '#')

# # Example usage
# draw_rectangle(30, 45)



def render(width, height):
    print('#' * width)

    for i in range(height-2):
            print('#' + ' ' * (width - 2) + '#')
    print('#' * width)

# Example usage
render(10, 5)