
./text2wfreq < limited_corpus.txt > data.wfreq
./wfreq2vocab < data.wfreq > data.vocab
./text2idngram -vocab data.vocab -temp . < limited_corpus.txt > data.idngram
./idngram2lm -idngram data.idngram -vocab data.vocab -context markers.ccs -arpa data.arpa
sphinx_lm_convert -i data.arpa -o data.lm.bin
mv data.lm.bin ../../pocketsphinx/model/en-us/
