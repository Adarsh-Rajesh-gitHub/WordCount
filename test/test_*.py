import sys
from pathlib import Path
from src.core import count_file



def test_WordCnt(capsys, tmp_path):
    d = tmp_path / 'test_dir'
    d.mkdir()
    p = d / 'hello.txt'
    p.write_text('Adventures of Huckleberry Finn is a classic American novel by Mark Twain, published in 1884, that follows the journey of a young boy, Huck Finn, and a runaway slave, Jim, down the Mississippi River. It\'s celebrated for its use of vernacular English, satirical critique of racism and hypocrisy in the antebellum South, and exploration of themes like freedom, morality, and societal norms through Huck\'s unique perspective. The book is a sequel to The Adventures of Tom Sawyer and is considered a masterpiece of American literature, despite its controversial language and themes. ')
    #check filename, number lines, words and characters
    res = count_file(str(p))
    assert  res.lines == 1
    assert res.words == 91
    assert res.chars == 578

