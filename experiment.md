temperature = 0.0 akan menghasilkan jawaban yang sama persis -> temperatur 0 = deterministik
top_p = 0.1 akan menghasilkan jawaban yang sama persis -> top_p sempit = konsisten

top_p = 1.0 akan menghasilkan jawaban yang sama persis -> temperatur tinggi = variatif
temperature = 1.5 akan menghasilkan jawaban yang lebih bervariatif -> top_p luas = variatif

sama" mengatur keacakan, jadi jangan gunakan keduanya sekaligus. hasilnya sama hanya mekanismenya saja yang berbeda


prompt engineering
instruksi/aturan main yang diterapkan kepada ai
yang bisa di kontrol lewat prompt-> 
1. persona("kamu adalah seorang...") menetukan role
2. format("selalu jawab dalam json...") menentukan format jawaban ai
3. batasan("jangan pernah membahas tentang politik...") membatasi jawaban ai
4. gaya bahasa("jawab singkat maksimal dalam 3 kalimat")
5. bahasa ("selalu gunakan bahasa indonesia...") menetapkan bahasa jawaban ai

few shoot: memberi contoh didalam prompt. dipakai ketika susah untuk dijelaskan dengan kata" namun mudah ditunjukkan dengan contoh.

chain of thought: meminta llm untuk menulis langkah berpikirnya sebelum menjawab, dapat meningkatkan akurasi untuk tugas penalaran. dipakai saat: soal mtk, soal logika, analisis multi-step, pengambilan keputusan dan agent reasoning.

structured output: meminta llm untuk mengembalikan output kedalam format terstruktur(json), bukan teks bebas.

Prompt engineering bukan "sihir". Ini kontrol. Semakin spesifik prompt, semakin terprediksi output. Untuk agent, kita butuh output yang bisa di-parse — karena itu structured output + validasi (extract_json) wajib.