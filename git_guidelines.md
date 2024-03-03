# How to create good commits

## Commit small

Do not create commits that are too large in scope because to makes them hard to read and this can make the intention of the commit become unclear. The same can be applied to pull requests and code in general. Smaller scope does not always mean less code but it means that the code you write, and therefore the commit, is used for one purpose.

## How to write good commit messages

1. Try to use imperative language
    - The title of your commit should be more like a command or a recipe
2. If the title of the commit isn't self-explanitory write a description
    - When you are writing a good description try to be concise and explain your reasoning or the purpose of your changes. For example when you are refactoring a function, say to make it more readable, you can explain the slight differences in for example signature changes or abstractions