---
title: "Pypapers: a bare-bones, command line,  PDF manager"
date: "2019-06-30"
categories: 
  - "culturalinformatics"
  - "techlife"
tags: 
  - "paper"
  - "python"
  - "reference_manager"
---

Ever felt like softwares like [Mendeley](https://www.mendeley.com/homepage-2-1?interaction_required=true&mboxSession=ea3c06ad39f14ce29d625b9d3be138c5) or [Papers](https://www.papersapp.com/) are great, but somehow slow you down? Ever felt like none of the many [reference manager softwares](https://en.wikipedia.org/wiki/Comparison_of_reference_management_software) out there will ever cut it for you, cause you need something R E A L L Y SIMPLE? I did. Many times. So I've finally crossed the line and tried out building a simple commmand-line PDF manager. [PyPapers](https://github.com/lambdamusic/pypapers), is called.

Yes - that's right - [command line](https://en.wikipedia.org/wiki/Terminal_(macOS)). So not for everyone. Also: this is bare bones and pre-alpha. So don't expect wonders. It basically provides a simple interface for searching a folder full of PDFs. That's all for now!

<iframe width="560" height="315" src="https://www.youtube.com/embed/o74Ct1EwZwI?controls=0" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

### Key features (or lack of)

- **Mac only, I'm afraid.** I'm sitting on the shoulders of a giant. That is, [mdfind](https://ss64.com/osx/mdfind.html).
- No fuss **search in file names** only or **full text**
- Shows all results and relies on [Preview](https://support.apple.com/en-gb/guide/preview/welcome/mac) for reading
- **Highlighting** on Preview works pretty damn fine and it's the ultimate compatibility solution (any other software kinds of locks you in eventually, imho)
- **Open source**. If you can code Python you can customise it to your needs. If you can't, open an [issue in github](https://github.com/lambdamusic/pypapers/issues) and I may end up doing it.
- It recognises **sub-folders**, so that can be leveraged to become a simple, filesystem level, categorization structure for your PDFs (eg I have different folders for articles, books, news etc..)
- Your PDFs live in the Mac **filesystem** ultimately. So you can always search them using Finder in case you get bored of the command line.

### First impressions

Pretty good. Was concerned I was gonna miss things like collections or tags. But I found a workaround: first, identify the papers I am interested in. Then, create a folder in the same directory and symlink them in there (= create an [alias](https://kb.iu.edu/d/achy)).

It's not quite like [uncarved wood,](https://www.taoistic.com/taoquotes/taoquotes-12-simplicity-stillness-silence.htm) but it definitely feels simple enough.
