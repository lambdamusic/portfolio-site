---
title: "Seminar: Tagore digital editions and Bengali textual computing"
date: "2011-10-13"
categories: 
  - "culturalinformatics"
tags: 
  - "bengali"
  - "collation"
  - "india"
  - "tagore"
  - "text-analysis"
---

Professor Sukanta Chaudhuri yesterday gave a very interesting talk on the scope, methods and aims of 'Bichitra' (literally, 'the various'), the ongoing project for an online variorum edition of the complete works of Rabindranath Tagore in English and Bengali. The talk (part of this year's [DDH research seminar](http://www.kcl.ac.uk/artshums/depts/ddh/events/newdh/index.aspx)) highlighted a number of issues I personally wasn't much familiar with, so in this post I'm summarising them a bit and then highlighting a couple of possible suggestions.

[Sukanta Chaudhuri](http://en.wikipedia.org/wiki/Sukanta_Chaudhuri) is Professor Emeritus at [Jadavpur University](http://www.jadavpur.edu/), Kolkata (Calcutta), where he was formerly Professor of English and Director of the [School of Cultural Texts and Records](http://www.jaduniv.edu.in/view_department.php?deptid=135). His core specializations are in Renaissance literature and in textual studies: he published [The Metaphysics of Text](http://www.amazon.co.uk/Metaphysics-Text-Sukanta-Chaudhuri/dp/0521197961) from Cambridge University Press in 2010. He has also translated widely from Bengali into English, and is General Editor of the [Oxford Tagore Translations](http://www.oup.co.in/category.php?cat_id=143772).

[Rabindranath Tagore](http://en.wikipedia.org/wiki/Rabindranath_Tagore) (1861 – 1941), the first nobel laureate of Asia, was arguably the most important icon of modern Indian Renaissance. This recent project on the electronic collation of Tagore texts, called 'the Bichitra project', is being developed as part of the national commemoration of the 150th birth anniversary of the poet (here's the [official page](http://rabindranathtagore-150.gov.in/index.html)). This is how the School of Cultural Texts and Records summarizes the project's scope:

> The School is carrying out pioneer work in computer collation of Tagore texts and creation of electronic hypertexts incorporating all variant readings. The first software for this purpose in any Indian language, named “Pathantar” (based on the earlier version “Tafat”), has been developed by the School. Two pilot projects have been carried out using this software, for the play Bisarjan (Sacrifice) and the poetical collection Sonar Tari (The Golden Boat). The CD/DVDs contain all text files of all significant variant versions in manuscript and print, and their collation using the ”Pathantar” software. The DVD of Sonar Tari also contains image files of all the variant versions. These productions are the first output of the series “Jadavpur Electronic Tagore”. Progressing from these early endeavours, we have now undertaken a two-year project entitled "Bichitra" for a [complete electronic variorum edition of all Tagores works in English and Bengali](http://rabindranathtagore-150.gov.in/online-voriourum.html). The project is funded by the Ministry of Culture, Government of India, and is being conducted in collaboration with Rabindra-Bhavana, Santiniketan. The target is to create a website which will contain (a) images of all significant variant versions, in manuscript and print, of all Tagores works; (b) text files of the same; and (c) collation of all versions applying the "Pathantar" software. To this end, the software itself is being radically redesigned. Simultaneously, manuscript and print material is being obtained and processed from Rabindra-Bhavana, downloaded from various online databases, and acquired from other sources. Work on the project commenced in March 2011 and is expected to end in March 2013, by which time the entire output will be uploaded onto a freely accessible website.

## A few interesting points

  
- Tagore, as Sukanta noted, "_wrote voluminously and revised extensively_". From a DH point of view this means that creating a comprehensive digital edition of his works would require **a lot of effort** - much more than what we could easily pay people for, if we wanted to mark up all of this text manually. For this reason it is fundamental to find some type of **semi-automatic methods for aligning and collating** Tagore's texts, e.g. the ”Pathantar” software. Follows a screenshot of the current collation interface.  
    [![Tagore digital editions](/media/static/blog_img/6241316162_5d5920dab8_z.jpg)](http://www.flickr.com/photos/mikele/6241316162/ "Tagore digital editions by MagIcReBirth, on Flickr")
- The [Bengali language](http://en.wikipedia.org/wiki/Bengali_language), which is used by Tagore, is widely spoken in the world (it is actually one of the most spoken languages, with nearly 300 million total speakers). However this language poses **serious problems for a DH project**. In particular, the [writing system](http://en.wikipedia.org/wiki/Bengali_script) is extremely difficult to parse using traditional OCR technologies: its vowel graphemes are mainly realized not as independent letters but as diacritics attached to its consonant letters. Furthermore clusters of consonants are represented by different and sometimes quite irregular forms, thus learning to read is complicated by the sheer size of the full set of letters and letter combinations, numbering about 350 (from [wikipedia](http://en.wikipedia.org/wiki/Bengali_script)).
- One of the critical points that emerged during the discussion had to do with the **visual presentation of the results of the collation** software. Given the large volume of text editions they're dealing with, and the potential vast amount of variations between one edition and the others, a powerful and interactive visualization mechanism seems to be **strongly needed**. However it's not clear what are the possible approaches on this front..
- **Textual computing**, Sukanta pointed out, is **not as developed in India** as it is in the rest of the world. As a consequence, in the context of the "Bichitra" project widely used approaches based on TEI and XML technologies haven't really been investigated enough. The collation software mentioned above obviously marks up the text in some way; however this markup remains hidden to the user and much likely it is not compatible with other standards. More work would thus be desirable in this area - in particular within the Indian continent.

## Food for thought

  
- **On the visualization of the results of a collation**. Some inspiration could be found in the type of visualizations normally used in [version control software systems](http://en.wikipedia.org/wiki/Revision_control), where multiple and alternative versions of the same file must be tracked and shown to users. For example, we could think of the visualizations available on GitHub (a popular code-sharing site), which are described on this [blog post](https://github.com/blog/39-say-hello-to-the-network-graph-visualizer) and demonstrated via an interactive tool on [this webpage](https://github.com/sr/git-wiki/network). Here's a screenshot:
    
    [![Github code visualization](/media/static/blog_img/6240800007_c2ed6467bb.jpg)](http://www.flickr.com/photos/mikele/6240800007/ "Github code visualization by MagIcReBirth, on Flickr")
    
    The [situation](http://betterexplained.com/articles/a-visual-guide-to-version-control/) is striking similar - or not? Would it be feasible to reuse one of these approaches with textual sources? Another relevant visualization is the one used by popular file-comparison softwares (eg File Merge on a Mac) for showing differences between two files:
    
    [![File Merge code visualization](/media/static/blog_img/6241316238_b2889f8c5a_z.jpg)](http://www.flickr.com/photos/mikele/6241316238/ "File Merge code visualization by MagIcReBirth, on Flickr")

- **On using language technologies with Bengali**. I did a quick tour of what's available online, and (quite unsurprisingly, considering the reputation Indian computer scientists have) found several research papers which seem highly relevant. Here's a few of them:
    
    \- _Asian language processing: current state-of-the-art_ \[[text](http://www.hlt.utdallas.edu/~vince/papers/lre06-intro.pdf)\] - _Research report on Bengali NLP engine for TTS_ \[[text](http://dspace.bracu.ac.bd/handle/10361/647)\] - The _Emile corpus_, containing fourteen monolingual corpora, including both written and (for some languages) spoken data for fourteen South Asian languages \[[homepage](http://www.lancs.ac.uk/fass/projects/corpus/emille/)\] - _A complete OCR system for continuous Bengali characters_ \[[text](http://ieeexplore.ieee.org/xpls/abs_all.jsp?arnumber=1273141&tag=1)\] - _Parsing Bengali for Database Interface_ \[[text](http://research.banglacomputing.net/iccit/ICCIT_pdf/5th%20ICCIT-2002_p277-p282.pdf)\] - _Unsupervised Morphological Parsing of Bengali_ \[[text](http://www.hlt.utdallas.edu/~vince/papers/lre06.html)\]
    
- **On open-source softwares that appear to be usable with Bengali text**. Not a lot of stuff, but more than enough to get started (the second project in particular seems pretty serious):
    
    \- [Open Bangla OCR](http://open-bangla-ocr.sourceforge.net/) - A BDOSDN (Bangladesh Open Source Development Network) project to develop a Bangla OCR - [Bangla OCR project](http://code.google.com/p/banglaocr/), mainly focused on the research and development of an Optical Character Recognizer for Bangla / Bengali script

Any comments and/or ideas?
