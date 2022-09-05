*In programming, a string is a sequence of characters. They are usually used to store data in text form. Here, we explore the string format in Python. We see how to create them as well as how to deal with strings that contain special characters through what is referred to as Escaping. I'll also introduce you to Kanye West's "greatest pain."*

- Strings are text surrounded by quotes  (single, double, or triple) quotes. 

```py
# Strings are text surrounded by quotes
# Both single (') or double (") or triple (""") quotes are used
# examples: "dinosaurs", '2112', "I'm lovin' it!"
```

> Here's another example using a variable: 

```py
kanye_quote = "my greatest pain in live is that I will never be able to see myself perform live"

print("kanye_quote")
```

*The command line will print out the string without the quotes. The Kanye quote is long, but if you want to break it up into multiple lines you can use triples-quotes `"""`:*

```py
...

kanye_quote = """My greatest pain in life
is that I will never be able
to see myself perform live."""

...
```

*But this will actually put newline breaks `(\n)` in between each line of the string. If you don't want those then you can avoid the newlines by putting a `\` at the end of each line, or simply by printing it with `print(kanye quote)` in the interpretive shell.*

## Escaping quotes in strings

*One problem is that if you want to put single or double-quotes inside your string, Python will think you're trying to end your string.*

*So if you want to use single or double-quotes in a string without closing it out, you have to "escape" it by putting a backslash (\) in front of it:*

```py
...

hamilton_quote = "Well, the word got around, they said, \"This kid's insane, man\""

print(hamilton_quote)
```

*It never hurts to put a `\` in front of a quotation mark. You can also add newlines or tabs to strings with `\n` and `\t`.*

*There are other characters you will need to escape. For example, in order to use a backslash in a string, you actually have to escape the backslash like this: `\\`.*

*Triple quotes are another way to use either single or double quotations within a string. Like so:*

```py
"""Well, the word got around, they said, "This kid's insane, man"""
```