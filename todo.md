# TODO – CSC17104 Final Project Workflow

> File này là bản hướng dẫn triển khai đồ án theo đúng 5 giai đoạn trong đề CSC17104 năm 2026. Mỗi giai đoạn ghi rõ việc cần làm, file thực hiện, đầu ra và điều kiện hoàn thành.
>
> **Nguyên tắc:** 3 Notebook chính theo đề là `01_collection_exploration.ipynb`, `02_analysis.ipynb`, `03_ml_question.ipynb`. Không cần tạo một Notebook riêng cho mỗi giai đoạn. Các file trong `docs/` là tài liệu quản lý bổ sung của nhóm.

## 0. Project setup – Chuẩn bị dự án

| Việc cần làm | File / vị trí | Đầu ra |
|---|---|---|
| Điền tên thành viên, mã số SV, GitHub | `README.md` | Bảng thành viên |
| Mô tả dự án và link Dataset | `README.md` | Project overview |
| Khai báo Python và thư viện | `environment.yml` | Conda environment dùng chung |
| Loại trừ file tạm và dữ liệu lớn | `.gitignore` | Git không commit dữ liệu lớn |
| Lưu dữ liệu gốc / dữ liệu xử lý | `data/raw/`, `data/processed/` | Thư mục dữ liệu |
| Ghi công việc, owner, deadline | `docs/PROJECT_PLAN.md` | Kế hoạch nhóm |
| Ghi nhật ký sử dụng AI | `LLM_USAGE.md` | Nhật ký LLM |

**Hoàn thành khi:** mọi thành viên clone được repo, tạo được Conda environment và mở Notebook bằng đúng kernel.

---

# 3.1. Data Collection – Thu thập dữ liệu

**File chính:** `notebooks/01_collection_exploration.ipynb`  
**Tóm tắt thông tin Dataset:** `README.md` (mục Dataset description / source / license).

### Cần làm gì?

- [ ] **Subject:** Dataset nói về chủ đề gì? Phản ánh bối cảnh thực tế nào? Một dòng đại diện cho đối tượng hay lần quan sát nào? Xác minh từ tài liệu nguồn.
- [ ] **Source:** Ghi URL Kaggle, tác giả / tổ chức công bố, nguồn dữ liệu gốc, ngày công bố / cập nhật / phiên bản nếu có.
- [ ] **License:** Ghi đúng thông tin Kaggle hiển thị: `Database: Open Database License (ODbL) 1.0; Contents: © Original Authors`. Đọc điều kiện attribution, share-alike và giới hạn áp dụng cho nội dung. Không mặc định mọi nội dung được cấp quyền giống Database.
- [ ] **Collection method:** Dữ liệu được thu thập bằng cách nào? Bao phủ đối tượng nào và khoảng thời gian nào? Có hạn chế hoặc bias nào được tài liệu nguồn nêu? Chỉ ghi điều có nguồn xác minh; nếu chưa tìm được thì ghi rõ chưa xác định.
- [ ] **Motivation:** Vì sao nhóm chọn Asteroid Dataset? Dataset có nhóm thông tin nào có tiềm năng phân tích và dự đoán?

### Viết ở đâu?

1. Viết đầy đủ bằng Markdown trong `01_collection_exploration.ipynb`.
2. Tóm tắt mô tả Dataset, nguồn, license và related work trong `README.md`.
3. Ghi URL tài liệu tham khảo trong phần References của Notebook / README.

### Đầu ra cần có

- [ ] Mô tả Dataset và ý nghĩa quan sát.
- [ ] Nguồn Kaggle và nguồn gốc dữ liệu được ghi rõ.
- [ ] License được giải thích đúng, có link.
- [ ] Phương pháp thu thập và giới hạn được xác minh hoặc ghi rõ chưa xác định.
- [ ] Lý do lựa chọn Dataset có lập luận.

---

# 3.2. Data Exploration – Khám phá dữ liệu

**File chính:** `notebooks/01_collection_exploration.ipynb`  
**Dữ liệu gốc:** `data/raw/` (không commit CSV lớn).  
**Dữ liệu sau xử lý nếu có:** `data/processed/`.

### Cần làm gì?

- [ ] **Overview:** Kiểm tra số dòng, số cột; giải thích một dòng đại diện cho gì; liệt kê tên cột, ý nghĩa, kiểu dữ liệu; xác định cột ID, numeric, categorical, thời gian (nếu có).
- [ ] **Numerical columns:** Thống kê count, mean, std, min, quartiles, max; khảo sát phân phối; kiểm tra min/max và đơn vị; phát hiện outlier bằng phương pháp phù hợp (IQR / Z-score); phân biệt giá trị cực đoan thật với lỗi.
- [ ] **Categorical columns:** Đếm số nhóm và tần suất; xem nhóm hiếm; kiểm tra nhãn không nhất quán / lỗi; cân nhắc gộp nhóm nếu có cơ sở.
- [ ] **Missing data:** Đếm số lượng và tỷ lệ thiếu từng cột; xem missing có quy luật không; đề xuất drop / impute / giữ nguyên / nhóm missing theo từng biến và giải thích.
- [ ] **Duplicates:** Kiểm tra dòng trùng hoàn toàn và ID trùng nếu phù hợp; xác minh trước khi xóa vì ID lặp có thể là quan sát hợp lệ.
- [ ] **Relationships:** Khảo sát tương quan, cross-tabulation, grouped statistics và biểu đồ cho các biến quan trọng; không cần tạo một biểu đồ cho mọi cột.
- [ ] **EDA summary:** Viết 3–5 phát hiện; nêu vấn đề chất lượng dữ liệu; kế hoạch preprocessing; các pattern có thể phát triển thành câu hỏi.

### Viết ở đâu?

1. Code, bảng, biểu đồ và nhận xét EDA nằm trong `01_collection_exploration.ipynb`.
2. File dữ liệu đã xử lý trung gian (nếu cần) lưu ở `data/processed/`, kèm mô tả cách tạo.
3. Tóm tắt Dataset trong `README.md` nếu cần.

### Đầu ra cần có

- [ ] Shape và ý nghĩa một dòng.
- [ ] Data dictionary / kiểu dữ liệu.
- [ ] Missing, duplicates, outliers đã được kiểm tra.
- [ ] Phân phối và quan hệ đáng chú ý được khảo sát.
- [ ] 3–5 nhận xét và preprocessing plan.
- [ ] Danh sách hướng câu hỏi tiềm năng.

**Lưu ý:** 3.2–3.4 là các giai đoạn iterative. Có thể quay lại EDA và thay đổi preprocessing / câu hỏi khi phát hiện dữ liệu không đáp ứng giả định ban đầu. Khi muốn quay lại thì nên thêm dữ liệu vào chứ đừng xóa bất cứ dữ liệu nào tại 6 câu hỏi thì mỗi người nên 2 câu nên có thể ảnh hưởng đến người khác 

---

# 3.3. Question Formulation – Xây dựng câu hỏi nghiên cứu

**File làm việc chi tiết:** `docs/QUESTION_BANK_TEMPLATE.md`  
**Danh sách câu hỏi chính thức:** `README.md`  
**Câu hỏi và motivation trước phần phân tích:** đầu mỗi section trong `02_analysis.ipynb` và `03_ml_question.ipynb`.

### Cần làm gì?

- [ ] Xác định số thành viên `3`; xây dựng đúng `3` câu hỏi.
- [ ] Mỗi thành viên phụ trách 2 câu hỏi.
- [ ] Có ít nhất 1 câu hỏi ML.
- [ ] Mỗi câu hỏi phải cụ thể, trả lời được bằng dữ liệu và có motivation: vì sao đáng nghiên cứu, ai quan tâm, kết quả hỗ trợ quyết định gì.
- [ ] Tránh câu hỏi quá dễ, chỉ cần một `groupby`, `value_counts`, `describe` và một biểu đồ.

### Với câu hỏi Non-ML

Mỗi câu phải sử dụng rõ ít nhất 2 tiêu chí; tổng các câu Non-ML phải bao phủ ít nhất 4/6 tiêu chí:

- [ ] **D1 – Combining data:** ghép bảng / Dataset; kiểm tra số dòng trước-sau và khóa không khớp.
- [ ] **D2 – Reshaping & time:** pivot / melt, resampling, rolling, lag hoặc so sánh theo kỳ nếu dữ liệu phù hợp.
- [ ] **D3 – Derived variables:** tạo biến mới có cơ sở từ cột gốc.
- [ ] **D4 – Controlling for a confounder:** kiểm tra quan hệ trong nhóm con hoặc kiểm soát biến thứ ba.
- [ ] **D5 – Quantifying uncertainty:** confidence interval, bootstrap, statistical test hoặc effect size.
- [ ] **D6 – Robustness check:** kiểm tra kết luận khi thay đổi quy tắc cleaning, ngưỡng outlier hoặc khoảng thời gian hợp lý.

Không cần ép dùng tiêu chí không phù hợp với Dataset; cần giải thích cách tiêu chí thực sự được áp dụng.

### Với câu hỏi ML

- [ ] Xác định prediction task, target và người dùng kết quả.
- [ ] Chọn features có sẵn tại thời điểm dự đoán.
- [ ] Liệt kê cột loại bỏ để tránh data leakage.
- [ ] Chọn cách chia dữ liệu phù hợp (time-based / group-based khi cần).
- [ ] Dự kiến ít nhất 2 ML models và 1 trivial baseline.
- [ ] Xác định metric, error analysis và model interpretation dự kiến.

### Viết ở đâu?

1. Dùng `docs/QUESTION_BANK_TEMPLATE.md` để brainstorm và ghi chi tiết từng câu.
2. Sau khi chốt, cập nhật bảng câu hỏi chính thức trong `README.md`: ID, nội dung, loại, owner, D criteria.
3. Đưa câu hỏi và motivation vào đầu phần tương ứng trong `02_analysis.ipynb` hoặc `03_ml_question.ipynb`.
4. Ghi owner và deadline trong `docs/PROJECT_PLAN.md`.

### Đầu ra cần có

- [ ] Đúng `6` câu hỏi.
- [ ] Mỗi người có 2 câu.
- [ ] Có ít nhất 1 câu ML.
- [ ] Mỗi câu Non-ML có ít nhất 2 D criteria.
- [ ] Tổng Non-ML bao phủ ít nhất 4/6 D criteria.
- [ ] Có motivation, owner và cột dữ liệu khả thi cho từng câu.

---

# 3.4. Data Analysis – Phân tích dữ liệu

## 3.4A. Non-ML analysis

**File chính:** `notebooks/02_analysis.ipynb`

Tạo một section riêng cho mỗi câu hỏi Q1, Q2, ...

### Với mỗi câu hỏi cần có

- [ ] Question & Motivation: câu hỏi, lý do nghiên cứu, owner.
- [ ] D criteria: nêu tiêu chí D1–D6 nào được dùng và dùng ở bước nào.
- [ ] Data & Variables: các cột, đơn vị, đối tượng phân tích.
- [ ] Preprocessing – Markdown: giải thích quy trình trước khi viết code.
- [ ] Preprocessing – Code: triển khai các bước đã mô tả.
- [ ] Row count checks: sau mỗi filter / merge / drop, ghi số dòng trước-sau và giải thích thay đổi.
- [ ] Analysis method – Markdown: giải thích phương pháp và lý do chọn.
- [ ] Analysis – Code: triển khai phương pháp.
- [ ] Results: trả lời trực tiếp bằng con số cụ thể.
- [ ] Visualizations: ít nhất 2 biểu đồ có title, axes, units, legend khi cần.
- [ ] Discussion: ý nghĩa thực tế, phát hiện bất ngờ và hạn chế.

Code dùng lại có thể chuyển thành hàm trong `src/`, nhưng Notebook vẫn phải giải thích quy trình và kết quả.

## 3.4B. Machine Learning analysis

**File chính:** `notebooks/03_ml_question.ipynb`

### Cần làm gì?

- [ ] Ghi câu hỏi ML và motivation.
- [ ] Định nghĩa prediction task, target, intended user và thời điểm dự đoán.
- [ ] Chọn features có sẵn tại prediction time.
- [ ] Liệt kê và loại bỏ leakage columns; giải thích lý do.
- [ ] Chọn train/test split phù hợp với cấu trúc dữ liệu.
- [ ] Đặt imputation / scaling / encoding trong scikit-learn Pipeline hoặc ColumnTransformer.
- [ ] Xây dựng một trivial baseline phù hợp.
- [ ] Xây dựng ít nhất 2 ML models phù hợp với regression / classification.
- [ ] Tuning bằng cross-validation chỉ trên training set.
- [ ] Chọn metric và giải thích lý do.
- [ ] Đánh giá test set một lần sau khi đã chọn mô hình.
- [ ] So sánh baseline và hai mô hình ML.
- [ ] Phân tích lỗi theo nhóm con / khoảng giá trị / ví dụ.
- [ ] Diễn giải mô hình (ví dụ permutation importance nếu phù hợp).
- [ ] Trả lời câu hỏi nghiên cứu ban đầu, không chỉ báo cáo score.

---

# 3.5. Summary and Reflection – Tổng kết và tự đánh giá

**Tổng kết chung:** có thể đặt ở section cuối của Notebook tổng hợp cuối cùng. Với cấu trúc hiện tại, nhóm có thể đặt phần này ở cuối `03_ml_question.ipynb`.  
**Tóm tắt findings:** `README.md`.  
**Reflection cá nhân:** khuyến nghị tạo `docs/REFLECTION.md` (file bổ sung do nhóm tổ chức; đề không chỉ định tên file riêng).

### Cần làm gì?

- [ ] **Key findings:** 3–5 phát hiện quan trọng từ toàn bộ Non-ML và ML; nhấn mạnh phát hiện bất ngờ nhất.
- [ ] **Limitations:** hạn chế của dữ liệu, phương pháp, giả định và phạm vi.
- [ ] **Future work:** câu hỏi, dữ liệu hoặc phương pháp có thể bổ sung nếu có thêm thời gian.
- [ ] **Individual reflection:** từng thành viên tự viết khó khăn và cách khắc phục, điều học được, cách sử dụng LLM.

### Viết ở đâu?

1. Tổng kết đầy đủ: cuối `03_ml_question.ipynb` hoặc Notebook tổng hợp cuối cùng.
2. Tóm tắt 3–5 findings: `README.md`.
3. Reflection từng người: `docs/REFLECTION.md`, mỗi người một mục.
4. Nhật ký AI: `LLM_USAGE.md`, ghi công cụ, câu hỏi và cách sử dụng / chỉnh sửa câu trả lời.

`docs/REFLECTION.md` là file bổ sung được khuyến nghị, không phải tên file bắt buộc trong đề.

---

# 4. Bảng đối chiếu nhanh: workflow và file

| Workflow | File chính | Nội dung |
|---|---|---|
| 3.1 Data Collection | `01_collection_exploration.ipynb` | Subject, source, license, collection method, motivation |
| 3.2 Data Exploration | `01_collection_exploration.ipynb` | Overview, types, numerical, categorical, missing, duplicates, relationships, EDA summary |
| 3.3 Question Formulation | `docs/QUESTION_BANK_TEMPLATE.md`, `README.md` | Brainstorm, motivation, D1–D6, ML task, owner |
| 3.4 Non-ML Analysis | `02_analysis.ipynb` | Preprocessing, method, results, ít nhất 2 plots mỗi câu |
| 3.4 ML Analysis | `03_ml_question.ipynb` | Pipeline, baseline, 2 ML models, tuning, test, errors, interpretation |
| 3.5 Summary & Reflection | Cuối `03_ml_question.ipynb`, `README.md`, `docs/REFLECTION.md` | Findings, limitations, future work, reflection cá nhân |

---

# 5. Các file bàn giao / hỗ trợ khác

| File / thư mục | Yêu cầu |
|---|---|
| `README.md` | Thành viên và IDs; ownership / task breakdown; Dataset, source, license, related public notebooks; questions; key findings; hướng dẫn chạy |
| `environment.yml` | Môi trường Conda và dependencies |
| `LLM_USAGE.md` | Công cụ, câu hỏi đã hỏi, cách sử dụng / chỉnh sửa câu trả lời |
| `data/raw/` | Dữ liệu gốc; không commit file lớn |
| `data/processed/` | Dữ liệu đã xử lý nếu cần |
| `src/` | Module Python tái sử dụng |
| `slides.pdf` | Slide thuyết trình |

---

# 6. Quy tắc làm việc nhóm

- [ ] Mỗi câu hỏi có một owner chính.
- [ ] Mỗi thành viên phụ trách 2 câu hỏi ( Non-ML) và 1 câu hỏi ML (Câu hỏi ML mình sẽ nói rõ sau )
- [ ] Làm việc trên branch riêng hoặc branch theo feature.
- [ ] Commit thường xuyên, message mô tả đúng thay đổi.
- [ ] Review trước khi merge vào `main`.
- [ ] Tránh nhiều người chỉnh cùng vùng Notebook cùng lúc.
- [ ] Chạy lại Notebook theo đúng thứ tự để kiểm tra kết quả.
- [ ] Mọi thành viên phải hiểu toàn bộ dự án, không chỉ phần mình viết.

---

# 7. Thứ tự triển khai đề xuất

1. Setup Repository, Conda, thông tin nhóm.
2. Hoàn thành 3.1 trong Notebook 01.
3. Khám phá Dataset theo 3.2 trong Notebook 01.
4. Brainstorm và chốt 3.3 trong Question Bank; cập nhật README.
5. Thực hiện các câu Non-ML theo 3.4A trong Notebook 02.
6. Thực hiện câu ML theo 3.4B trong Notebook 03.
7. Hoàn thành 3.5: findings, limitations, future work, reflection.
8. Hoàn thiện README, LLM_USAGE, environment, slides và kiểm tra Repository.

> **Lưu ý về tính lặp:** Đề nói các giai đoạn 3.2–3.4 có tính iterative. Thứ tự trên giúp quản lý công việc; không có nghĩa là cấm quay lại EDA, preprocessing hoặc điều chỉnh câu hỏi khi có phát hiện mới.
