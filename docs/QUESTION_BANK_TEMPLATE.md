# Ngân hàng câu hỏi nghiên cứu

## Bộ đề xuất Q1–Q4 theo D1–D4

Theo yêu cầu đã chốt: **cả bộ bao phủ D1–D4, mỗi câu dùng ít nhất hai tiêu chí**.
Các câu đã chạy trong Notebook 02, chờ nhóm duyệt. Chưa coi là phân công chính
thức; điền tên người phụ trách sau khi nhóm thống nhất. D5/D6 không phải tiêu
chí của bộ này; mẫu tổng quát phía dưới vẫn được giữ cho công việc sau.

| ID | Câu hỏi cụ thể | Tiêu chí | Cách thực hiện |
|---|---|---|---|
| Q1 | Sau khi ghép phân loại phổ SMASSII từ JPL vào dataset, nhóm phổ C và S có tỷ lệ albedo dưới 0,10 chênh lệch bao nhiêu điểm phần trăm khi so sánh cùng khoảng đường kính? | D1, D3, D4 | Ghép bảng JPL có spec_B với Kaggle theo pdes; kiểm tra 1–1, khóa không khớp; tạo nhóm C/S, cờ albedo thấp và chuẩn hóa khoảng đường kính. |
| Q2 | Trong từng khoảng độ sáng tuyệt đối H, nhóm NEO và không-NEO có tỷ lệ được ghi nhận đường kính, albedo và độ bất định đường kính khác nhau thế nào? Nhóm nào có tỷ lệ đủ cả H–đường kính–albedo cao hơn? | D2, D3, D4 | Tạo cờ có từng số đo/đủ bộ; melt bảng rộng thành dài, pivot để đối chiếu; so sánh NEO theo cùng khoảng H. |
| Q3 | Với các đối tượng có đủ H, albedo và đường kính, nếu tính đường kính từ H với albedo cố định 0,15, kết quả thường cao hay thấp hơn đường kính ghi nhận bao nhiêu phần trăm, và khác nhau thế nào giữa các nhóm albedo? | D3, D4 | Dùng công thức JPL tạo đường kính ước lượng, lệch có dấu/tuyệt đối; phân tích theo nhóm albedo và lớp quỹ đạo. |
| Q4 | So với MBA, OMB và TJN có tỷ lệ đối tượng có albedo dưới 0,10 chênh lệch bao nhiêu điểm phần trăm khi so sánh cùng khoảng đường kính? | D3, D4 | Tạo cờ albedo <0,10; so sánh OMB−MBA và TJN−MBA trong cùng cơ cấu khoảng đường kính. |

Q1 bổ sung nhãn phổ thật sự, không tách rồi ghép lại một bảng để gán D1. Nhãn
phổ JPL ở thời điểm tải không phải nhãn lịch sử của snapshot Kaggle. Q2 dùng
reshaping cho so sánh nhiều số đo, không suy năm phát hiện từ epoch. Q3 là
hệ quả của công thức đã biết, không phải kiểm định dự báo độc lập. Q4 chỉ kết
luận trong tập có số đo và vùng chung riêng của từng cặp.

## Mẫu để nhóm tiếp tục bổ sung câu hỏi

## Question ID: Q__

- **Exact research question:**
- **Type:** Non-ML / ML
- **Owner:**
- **Motivation:** Why is this worth answering?
- **Intended audience / user:**
- **Decision informed by the answer:**
- **Dataset columns required:**
- **Potential data limitations:**
- **Proposed method:**
- **Expected output / at least two plot ideas:**
- **Related prior work and how this question differs:**

### For Non-ML questions

- **D1 – Combining data:** Yes / No. Explain.
- **D2 – Reshaping & time:** Yes / No. Explain.
- **D3 – Derived variables:** Yes / No. Explain.
- **D4 – Controlling for a confounder:** Yes / No. Explain.
- **D5 – Quantifying uncertainty:** Yes / No. Explain.
- **D6 – Robustness check:** Yes / No. Explain.

At least two criteria must be clearly used by this question.

### For the ML question

- **Prediction target:**
- **Who uses the prediction and when:**
- **Features available at prediction time:**
- **Columns excluded to prevent leakage:**
- **Split strategy and justification:**
- **Baseline:**
- **ML model 1:**
- **ML model 2:**
- **Cross-validation / tuning plan:**
- **Evaluation metric and justification:**
- **Error analysis plan:**
- **Model interpretation plan:**
