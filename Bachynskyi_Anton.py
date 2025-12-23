# .bachynskyi_exam
import sys
try:
    import cgi
except ImportError:
    import legacy_cgi as cgi

from googletrans import Translator

lang = "Ukrainian"

RED = "\033[31m"
BLUE = "\033[34m"
RESET = "\033[0m"

translator = Translator()

def get_text(text, target_lang):
    """Перекладає текст, якщо обрано не українську мову"""
    if target_lang.lower() in ["ukrainian", "uk"]:
        return text
    try:
        return translator.translate(text, src='uk', dest=target_lang).text
    except:
        return text

def main():
    prompt = get_text("Введіть довжини сторін трикутника a, b, c: ", lang)
    exists_msg = get_text("Трикутник з сторонами {} існує.", lang)
    iso_part = get_text("є рівнобедреним", lang)
    reason_part = get_text("так як дві його сторони дорівнюють", lang)
    intro_part = get_text("Трикутник з сторонами", lang)

    user_input = input(prompt)
    try:
        sides = [float(x) for x in user_input.split()]
        if len(sides) != 3: raise ValueError
        a, b, c = sides
    except ValueError:
        print("Помилка вводу!")
        return

    def f(n): return str(int(n) if n.is_integer() else n)

    if (a + b > c) and (a + c > b) and (b + c > a):
        sides_blue = f"{BLUE}{f(a)},{f(b)},{f(c)}{RESET}"
        print(exists_msg.format(sides_blue))

        equal_side = None
        if a == b: equal_side = a
        elif a == c: equal_side = a
        elif b == c: equal_side = b

        if equal_side is not None:
            sides_red = f"{RED}{f(a)}, {f(b)}, {f(c)}{RESET}"
            blue_iso = f"{BLUE}{iso_part}{RESET}"
            red_value = f"{RED}{f(equal_side)}{RESET}"
            
            print(f"{intro_part} {sides_red} {blue_iso} {reason_part} {red_value}.")
    else:
        print(get_text("Трикутник не існує.", lang))

if __name__ == "__main__":
    main()