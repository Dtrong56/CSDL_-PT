# CSDL_-PT-GK
Project cuối EX6
Đề :
5. As a project, write a program that implements inverted indexes. Your program must contain the following routines:
(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

Câu a -Nguyễn Thành Long N21DCCN143:
Nhận đầu vào là:

    Dir: thư mục chứa các văn bản.

    StopList: tên file chứa danh sách từ dừng.

Tạo:

    DocTable: danh sách tất cả file trong Dir (ngoại trừ StopList).

    TermTable: inverted index, chỉ chứa các từ bắt đầu bằng chữ C/c, không nằm trong StopList.