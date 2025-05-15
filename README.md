# CSDL_-PT-GK
Sinh viên thực hiện:
Nguyễn Thành Long	N21DCCN143     Câu a
Thạch Thị Nhanh	    N21DCCN159     Câu b
Vũ Đức Trọng	    N21DCCN190     Câu c
Lê Anh Tình	        N21DCCN189???

Hướng dẫn cài đặt: git clone...
Hướng dẫn chạy chương trình: chạy program.py

Project cuối EX6
Đề :
5. As a project, write a program that implements inverted indexes. Your program must contain the following routines:
(a) CreateIndex(Dir, StopList) takes a directory name and a file called StopList (in that directory) as input. It returns an inverted index as output. The DocTable includes all files in the directory Dir, except for the StopList file. The TermTable includes only all words occurring in the directory that start with the letter C (lower- or uppercase).

(b) Find(Word, Weight, N) finds the top N documents in the index associated with the word specified in the input.

(c) Find(WordFile, N) is similar to the above, but there is one difference. Instead of taking a single word as part of the input, it takes a file called WordFile as input. This file has, on each line, a word (string) and a weight (integer). It then attempts to find, using the inverted index, the top N matches for this query.

Câu a -Nguyễn Thành Long N21DCCN143:
    Viết hàm CreateIndex(Dir, StopList):

        Đọc toàn bộ file trong thư mục Dir, trừ StopList.

        Chỉ lưu từ bắt đầu bằng chữ C hoặc c (case-insensitive).

        Bỏ qua các từ nằm trong StopList.

        Trả về chỉ mục đảo.
    Input:
        Dir: thư mục chứa các văn bản.
        StopList: tên file chứa danh sách từ dừng.
    Output:
        DocTable: danh sách tất cả file trong Dir (ngoại trừ StopList).
        TermTable: inverted index, chỉ chứa các từ bắt đầu bằng chữ C/c, không nằm trong StopList.
    Ví dụ:
        Thư mục: documents/
            Chứa các file sau: Là Input Dir
                documents/
                ├── stoplist.txt
                ├── doc1.txt
                └── doc2.txt
            Input stoplist.txt gồm:
                is
                the
                on
                and
                a
                with
            File doc1.txt gồm:
                The cat is sleeping on the couch.
                Clouds cover the sky and it is cold.
            FIle doc2.txt gồm:
                A clever cat climbs carefully.
                The cloud is moving fast.
        Output: 
            DocTable:
            {
                0: "doc1.txt",
                1: "doc2.txt"
            }
            TermTable:
            {
            'cat': {'doc1.txt': 1, 'doc2.txt': 1},
            'couch': {'doc1.txt': 1},
            'clouds': {'doc1.txt': 1},
            'cloud': {'doc2.txt': 1},
            'clever': {'doc2.txt': 1},
            'climbs': {'doc2.txt': 1},
            'carefully': {'doc2.txt': 1},
            'cover': {'doc1.txt': 1},
            'cold': {'doc1.txt': 1}
            }