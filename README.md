# TrutleFractal

Create a fractal using LGrammar

# Example L-Grammars

## Binary Tree

```python
initialHeading = 90
gen = 3
scale = 1 / 2
windowSize = 500
size = windowSize * scale ** (gen)
axiom = "F"
Lgrammar = {
    "F": "F[-F][+F]",
    "f": "",
    "X": "",
    "Y": "",
    "U": "",
    "V": "",
}
angle = 30
```

## Koch Curve

```python
initialHeading = 0
gen = 3
scale = 1 / 3
windowSize = 500
size = windowSize * scale ** (gen)
axiom = "F"
Lgrammar = {
    "F": "F-F++F-F",
    "f": "",
    "X": "",
    "Y": "",
    "U": "",
    "V": "",
}
angle = 60
```

## Quadratic Koch Curve

```python
initialHeading = 0
gen = 3
scale = 1 / 4
windowSize = 500
size = windowSize * scale ** gen
axiom = "F+F+F+F"
Lgrammar = {
    "F": "F+F-F-FF+F+F-F",
    "f": "",
    "X": "",
    "Y": "",
    "U": "",
    "V": "",
}
angle = 90
```

## Quadratic Koch Curve

```python
initialHeading = 0
gen = 3
scale = 1 / 3
windowSize = 500
size = windowSize * scale ** (gen)
axiom = "X"
Lgrammar = {
    "F": "F",
    "f": "",
    "X": "-YF+XFX+FY-",
    "Y": "+XF-YFY-FX+",
    "U": "",
    "V": "",
}
angle = 90
```

## Dragon Curve

```python
initialHeading = 0
gen = 3
scale = 1 / 2
windowSize = 500
size = windowSize * scale ** (gen)
axiom = "X"
Lgrammar = {
    "F": "F",
    "f": "",
    "X": "X+YF+",
    "Y": "-FX-Y",
    "U": "",
    "V": "",
}
angle = 90
```
