import pygame
import render

# Window dimensions
window = render.render(False)
window.setBackgroundColor(window.colors.black)
window.arrow_size = 7
window.draw_axes(window.colors.white)

def main():
	running = True
	while running:
		running = window.check_for_exit()	


if __name__ == "__main__":
	main()
