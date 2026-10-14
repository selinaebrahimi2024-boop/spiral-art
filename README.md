# spiral-art
spiral art project
# Spiral Art

A small Python project that uses the built-in `turtle` module to draw a colorful spiral pattern on a black background. I made it as a practice exercise while learning Python and basic graphics programming.

## Preview

![Spiral Art Preview](preview.png)

*(Add a screenshot of your drawing as `preview.png` in the project folder.)*

## Features

- Black canvas with a custom window title
- Six cycling colors: red, pink, purple, yellow, orange, green
- Fastest drawing speed (`speed(0)`)
- Window closes on click

## Requirements

- Python 3.x
- `turtle` (included in Python's standard library, no installation needed)
  - On some Linux systems you may need to install `python3-tk`.

## How to Run

```bash
python spiral_art.py
```

Click on the window when the drawing finishes to close it.

## How It Works

The turtle repeats the same two steps 100 times:

1. Move forward by a distance that grows with each step (`i * 2`).
2. Turn left by a fixed angle (`120°`).

Because the side length keeps increasing while the turning angle stays the same, the path never closes. Instead, it spirals outward. The pen color changes on every step using `colors[i % len(colors)]`, which loops through the color list.

## Experiment: Changing the Angle

The turning angle controls which polygon the spiral is built from. With a turn of `360 / n` degrees, the pattern forms an *n*-sided polygon spiral. Try changing this line:

```python
pen.left(120)
```

| Angle | Resulting shape |
|-------|-----------------|
| `120` | Triangle spiral (default) |
| `90`  | Square spiral |
| `72`  | Pentagon spiral |
| `60`  | Hexagon spiral |
| `45`  | Octagon spiral |
| `144` | Star-like (pentagram) spiral |

Angles that are not a clean divisor of 360 (for example `91` or `119`) produce twisting, swirling patterns, because each new line is rotated slightly compared to the previous round.

## Code

```python
import turtle

boom = turtle.Screen()
boom.bgcolor("black")
boom.title("selina")

pen = turtle.Turtle()
pen.speed(0)

colors = ["red", "pink", "purple", "yellow", "orange", "green"]

for i in range(100):
    pen.pencolor(colors[i % len(colors)])
    pen.forward(i * 2)
    pen.left(120)

boom.exitonclick()
```

## Ideas for Improvement

- Ask the user for the angle with `turtle.numinput`
- Add more colors or random colors
- Increase the number of steps for denser patterns
- Hide the turtle cursor with `pen.hideturtle()`

## License

This project is open source and available under the MIT License.
