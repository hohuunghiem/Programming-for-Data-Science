# Nhãn phổ bổ sung cho Q4

`jpl_smassii_taxonomy.json` là bản kết quả đã lưu từ NASA/JPL SBDB Query API, gồm
1.666 dòng với các trường `spkid`, `pdes`, `spec_B`. `spec_B` là loại phổ SMASSII.
Q4 ghép bằng `pdes`; chỉ dùng nhãn đúng bằng C hoặc S khi so sánh albedo.

- Nguồn và định nghĩa trường: https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html
- Thời điểm tải bản này: `2026-11-21T20:41:04.929645+00:00` (UTC).
- URL truy vấn chính xác, số dòng và SHA-256 nằm trong `jpl_smassii_metadata.json`.
- Truy vấn yêu cầu `fields=spkid,pdes,spec_B` và điều kiện `spec_B` có dữ liệu.

Notebook đọc bản đã lưu và kiểm tra SHA-256, không tự cập nhật nguồn trên Internet.
Ngày tải JPL không phải ngày đo mọi thuộc tính. Bản Kaggle và JPL có thể khác thời điểm;
ghép được mã không chứng minh rằng nhãn đã có ở thời điểm tạo CSV.

Để chạy: đặt CSV gốc tại `data/raw/dataset.csv`, mở `notebooks/02_analysis.ipynb`,
chạy ô nạp `df_raw` đầu notebook rồi chạy Q4, hoặc chạy toàn bộ notebook.
Không cần thư mục `Kiet-learning` bên ngoài repo. CSV thô không được đưa vào Git.
