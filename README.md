#Quill - quill-doc

<p align="center">
  <img src="Quill_logo.png" width="150" alt="Quill Logo">
</p>

![License: Non-Commercial](https://img.shields.io/badge/License-Non--Commercial-orange.svg)
![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)
![Build Status](https://img.shields.io/badge/status-active-brightgreen.svg)

I created **Quill** because, frankly, I don't document anything. As a student, I realized I needed a simple project to keep track of my code and allow my team to understand what I did (and vice versa) without the friction of manual docs.

Quill bridges the gap: write your code, tell Quill what you did, and it handles the organization. It tracks your classes, functions, and structs so your team is never lost.

---

## How to use it

### Prerequisites
* **Git:** Ensure you have [Git installed](https://git-scm.com/) and have run `git init` in your project folder.
* **Python:** Version 3.8 or higher.

### Installation
Right now, Quill is available via pip:
```bash
pip install quill-doc
```


  **Initialize Quill** in your project root:
    ```bash
    quill init
    ```

 **Commit your code** using your standard Git workflow (e.g., `git add .` and `git commit -m "your message"`).

  **Document your changes**: After every commit, run:
    ```bash
    quill run
    ```
  **Input & Save**: When prompted for input, describe your changes. Use the keyword **DONE** to exit and save.

> **Note:** Your documentation is automatically saved in the `.quill` folder inside `project_documentation.md` and tracked via `index.json`.


### Languages To-Do

I am a student looking to improve my skills and eventually support all major languages. If you have advice on how i can improve the tool, please reach out!

#### Language Support
- [x] Python
- [x] C++
- [x] JavaScript
- [ ] C
- [ ] TypeScript
- [ ] Ruby
- [ ] Java
- [ ] Dart
- [ ] Rust

## License & Ethics

This project is shared under a **Custom Non-Commercial License**.

* ✅ **Use & Share**: Free for anybody who wants to use it .
* ❌ **No Resale**: You may not sell this code or profit from it.

> I built this as my portfolio project to give back to the open-source community that has helped me so much. It may not be great but i hope its useful to people and I'll continue to work on it


## A BIG Shout Out To :

A massive thank you to the giants whose shoulders this project stands on. These libraries made the heavy lifting possible (even if I still lost a significant amount of hair in the process):

* **[Tree-sitter](https://tree-sitter.github.io/tree-sitter/)**: For the incredible incremental parsing that helps Quill understand your code.
* **[Rich](https://github.com/Textualize/rich)**: For making the terminal output look beautiful and readable.
* **[Typer](https://typer.tiangolo.com/)**: For making the CLI interface development a breeze.
* **[Git](https://git-scm.com/)**: The backbone of everything we do.

> **Developer Note:** While these tools made the project "easier," I'd like to officially apologize to my barber as this is my first major project and I lost a ton of hair. This project was built with 10% Python and 90% pure stress.
