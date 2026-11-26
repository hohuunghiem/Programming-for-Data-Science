# Dữ liệu bổ sung từ NASA/JPL

## Nhãn phổ cho Q4

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

## Chu kỳ tự quay cho Q6

`jpl_rotation_periods.json` chứa 34.592 bản ghi từ
[NASA/JPL SBDB Query API](https://ssd-api.jpl.nasa.gov/doc/sbdb_query.html).
Truy vấn lấy `pdes` và `rot_per` của các tiểu hành tinh có chu kỳ tự quay dương.
`rot_per` là chu kỳ tự quay biểu kiến, tính bằng giờ.

- Thời điểm tải: `2026-11-25T15:52:15.9113606+00:00` (UTC).
- URL truy vấn, trường dữ liệu và số bản ghi nằm trong JSON.
- SHA-256: `f548b7cc3d119600fc2c27927e37f1f134010aeacdaab4514bcf612aa5d786c8`.

Q6 trong [Notebook 03](../../notebooks/03_ml_question.ipynb) ghép bản chụp này với
`data/raw/dataset.csv` theo `pdes`. Đặt CSV gốc theo hướng dẫn trong README và
chạy notebook từ thư mục gốc hoặc `notebooks/`.
