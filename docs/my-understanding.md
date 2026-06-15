# My Understanding — Author's Notes

This file is a working notebook where I explain the project's analytical choices **in my own words, in plain language**, as I learn them. It complements the formal documents (`charter.md`, `methodology.md`, `data_collection.md`) — those are the canonical specs; this file is where I make sure I actually understand them.

Write in English (per the project's English-only policy for committed artifacts).

Treat this file as if you were explaining the project to a fellow demand planner over coffee. If you cannot explain a section without falling back on jargon or hand-waving, that's a signal to revisit the formal docs and come back to this file.

---

## 1. Data approach

> _What data are we using? Why this particular data source? What does the data physically look like (granularity, span, format)? If a planner asked "where do these numbers come from?", what would you say?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §1, `docs/data_collection.md`.

---

## 2. Normalization logic

> _Google Trends returns values on a 0 – 100 scale per file. Why does that matter? What does "scale-invariant ratio" actually mean for our metrics? Which comparisons does the per-file normalization allow, and which does it block? When someone asks "why can't I just say beer was 30% more popular in 2024 than 2020," what's the answer?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §4.6, §5 (limitation L2).

---

## 3. Tet windowing

> _How do we define the "Tet window" each year? Why 6 weeks pre-Tet and 4 weeks post-Tet? What is `T` exactly, and why does it shift on the Gregorian calendar? How would the analysis change if we used a 4-week pre-window instead — would the framework still answer the same question?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §3.

---

## 4. Metrics calculation

> _Walk through each of the four core metrics in plain language:_
> - _Build-up uplift % — what does it answer? how is it computed? what value is "high" vs "low"?_
> - _Holiday dip % — same questions._
> - _Recovery time (weeks) — same._
> - _Peak timing (weeks before T) — same._
>
> _For a Tet-sensitive category (e.g. confectionery), what pattern across the four metrics would you expect to see? What about a Tet-neutral category?_

[ write your notes here ]

**Related canonical docs:** `docs/methodology.md` §4.1 – §4.4.

---

## Open questions for myself

> _Things I think I understand but want to verify. Things I do not yet understand and want to revisit. Things that are genuinely fuzzy and need an outside check._

[ write your notes here ]

---

## Defend Notes — planner challenges (interview prep)

Câu chất vấn của một demand planner + câu trả lời để defend. Ghi bằng tiếng Việt để ôn nhanh.

> Hai điểm dễ tổn thương nhất: **#1 (search ≠ sales)** và **#3 (per-file normalization)**. Nắm chắc hai cái này, phần còn lại nhẹ nhàng.

**1. "Search không phải sales — sao tin được con số phản ánh nhu cầu thật?"**
KHÔNG claim search = sales. Chỉ claim *shape* (hình dạng theo thời gian) của search ≈ shape của demand. Tết effect là phép đo *tương đối* (uplift so với baseline của chính category đó), nên chỉ cần shape đúng, không cần mức tuyệt đối. Đóng khung mọi kết luận là "search-implied — để planner đối chiếu với sales nội bộ", không thay thế. Framing khiêm tốn này chính là thứ làm nó đáng tin.

**2. "Sao không dùng Nielsen/Kantar/GSO — đó mới là sales thật?"**
Đã thử, không khả thi ở độ phân giải cần. GSO chỉ monthly + aggregate trên mức category; Nielsen/Kantar paywall. Google Trends là nguồn duy nhất vừa free, weekly, public, reproducible, vừa phủ đủ 6 năm — planner tự rerun kiểm chứng được. Điểm mạnh, không phải đường tắt.

**3. "Per-file normalization — vậy 130% có thật hay artifact?"**
Defend bằng toán. Mỗi file normalize = nhân toàn bộ giá trị với hằng số chưa biết `k`. Lấy (trung bình cửa sổ Tết) ÷ (trung bình baseline) *trong cùng một file* → `k` ở cả tử và mẫu → triệt tiêu. Nên uplift % không bị ảnh hưởng. Cái KHÔNG làm được là so mức tuyệt đối giữa năm/category — và không bao giờ claim điều đó. Nhấn mạnh: mọi số đều là tỷ lệ trong cùng file.

**4. "Heuristic của tôi là 4 tuần, data nói 1–2 tuần. Ai sai?"**
Đừng nói heuristic sai. 4 tuần có thể là lúc demand *bắt đầu* tăng; *đỉnh* rơi ở T−1 đến T−2 tuần. Hai con số đo hai thứ khác nhau. Đây là tinh chỉnh, không phủ định kinh nghiệm planner — giữ thiện cảm.

**5. "Dữ liệu chỉ là dân thành thị, trẻ, online — Tết tiêu thụ mạnh ở nông thôn?"**
Thừa nhận thẳng (limitation L3). Đóng khung là "urban-skewed Tết effect". Nông thôn nặng bánh kẹo, bia, dầu ăn → uplift thật có thể còn *cao hơn* số đo được, không thấp hơn. Hướng sai lệch là conservative.

**6. "6 năm có 2 năm COVID — có méo kết quả không?"**
2020 và 2021 luôn report riêng, không trộn vào mean nếu không có caveat (L5). Đã thử STL để tách COVID nhưng trung thực báo cáo *không tách sạch được* — residual lớn nhất thực ra ở 2023/2024 do lunar-calendar drift, không phải COVID. Sự trung thực này tăng độ tin cậy.

---

**Last updated:** 2026-06-15
