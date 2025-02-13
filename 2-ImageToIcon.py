from PIL import Image
import sys
import os

def main():
	if len(sys.argv) != 2:
		print("Uso: py 2-ImageToIcon.py imagen.png")
		return

	img_path = sys.argv[1]
	if not os.path.isfile(img_path):
		print(f"Error: '{img_path}' no existe.")
		return

	icon_path = os.path.splitext(img_path)[0] + ".ico"
	try:
		Image.open(img_path).convert("RGBA").save(
			icon_path, format="ICO",
			sizes=[(16,16),(32,32),(48,48),(64,64),(128,128),(256,256)]
		)
		print(f"Icono creado exitosamente: {icon_path}")
	except Exception as e:
		print(f"Error: {e}")

if __name__ == "__main__":
	main()