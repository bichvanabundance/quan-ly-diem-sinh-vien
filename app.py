
#1. IMPORT THU VIEN

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


#2. TAO DU LIEU 10 SINH VIEN

data = {
    "Ho_ten": [
        "Nguyen Van An",
        "Tran Thi Binh",
        "Le Hoang Nam",
        "Pham Minh Anh",
        "Vo Thanh Dat",
        "Do Ngoc Ha",
        "Bui Quang Huy",
        "Hoang Thu Linh",
        "Dang Gia Bao",
        "Nguyen Mai Chi"
    ],
    "MSSV": [
        "SV001", "SV002", "SV003", "SV004", "SV005",
        "SV006", "SV007", "SV008", "SV009", "SV010"
    ],
    "Chuyen_can": [9, 8, 10, 7, 6, 9, 8, 10, 5, 7],
    "Giua_ky":    [8, 7, 9, 8, 6, 8, 7, 9, 5, 6],
    "Cuoi_ky":    [9, 8, 9, 7, 5, 9, 8, 10, 4, 7]
}

df = pd.DataFrame(data)


#3. TINH DIEM TONG KET

df["Tong_ket"] = (
    0.2 * df["Chuyen_can"]
    + 0.3 * df["Giua_ky"]
    + 0.5 * df["Cuoi_ky"]
).round(2)


#4. XEP LOAI SINH VIEN

def xep_loai(diem):
    if diem >= 8.5:
        return "Gioi"
    elif diem >= 7.0:
        return "Kha"
    elif diem >= 5.0:
        return "Trung binh"
    else:
        return "Yeu"

df["Xep_loai"] = df["Tong_ket"].apply(xep_loai)


#5. CAU HINH TRANG WEB

st.set_page_config(
    page_title="Quan ly diem sinh vien",
    page_icon="📚",
    layout="wide"
)

st.title("QUẢN LÝ ĐIỂM SINH VIÊN")
st.write("Bảng điểm, thống kê và xếp loại sinh viên.")


#6. HIEN THI BANG DIEM

st.subheader("1. Bảng điểm của 10 sinh viên")

bang_hien_thi = df[
    ["Ho_ten", "Chuyen_can", "Giua_ky",
     "Cuoi_ky", "Tong_ket", "Xep_loai"]
].rename(columns={
    "Ho_ten": "Họ tên",
    "Chuyen_can": "Chuyên cần",
    "Giua_ky": "Giữa kỳ",
    "Cuoi_ky": "Cuối kỳ",
    "Tong_ket": "Tổng kết",
    "Xep_loai": "Xếp loại"
})

st.dataframe(bang_hien_thi, use_container_width=True)


#7. THONG KE DIEM

diem_tb = df["Tong_ket"].mean()
sv_max = df.loc[df["Tong_ket"].idxmax()]
sv_min = df.loc[df["Tong_ket"].idxmin()]
so_sv_dat = int((df["Tong_ket"] >= 5).sum())

st.subheader("2. Thống kê kết quả học tập")

cot1, cot2, cot3 = st.columns(3)

cot1.metric("Điểm trung bình lớp", f"{diem_tb:.2f}")
cot2.metric("Số sinh viên đạt", f"{so_sv_dat}/10")
cot3.metric("Tổng số sinh viên", len(df))

st.write(
    f"**Điểm cao nhất:** {sv_max['Ho_ten']} "
    f"({sv_max['Tong_ket']:.2f} điểm)"
)

st.write(
    f"**Điểm thấp nhất:** {sv_min['Ho_ten']} "
    f"({sv_min['Tong_ket']:.2f} điểm)"
)


#8. CHON SINH VIEN BANG SELECTBOX

st.subheader("3. Tra cứu điểm từng sinh viên")

ten_sv = st.selectbox(
    "Chọn một sinh viên:",
    df["Ho_ten"].tolist()
)

sv = df[df["Ho_ten"] == ten_sv].iloc[0]

st.write(f"**Họ tên:** {sv['Ho_ten']}")
st.write(f"**Điểm chuyên cần:** {sv['Chuyen_can']}")
st.write(f"**Điểm giữa kỳ:** {sv['Giua_ky']}")
st.write(f"**Điểm cuối kỳ:** {sv['Cuoi_ky']}")
st.write(f"**Điểm tổng kết:** {sv['Tong_ket']:.2f}")
st.write(f"**Xếp loại:** {sv['Xep_loai']}")


#9. VE BIEU DO COT

st.subheader("4. Biểu đồ điểm tổng kết của 10 sinh viên")

fig, ax = plt.subplots(figsize=(12, 5))

ax.bar(df["Ho_ten"], df["Tong_ket"])
ax.set_title("Điểm tổng kết của 10 sinh viên")
ax.set_xlabel("Họ tên sinh viên")
ax.set_ylabel("Điểm tổng kết")
ax.set_ylim(0, 10)
ax.tick_params(axis="x", rotation=45)

fig.tight_layout()
st.pyplot(fig)
plt.close(fig)


#10. THONG TIN NGUOI TAO UNG DUNG

st.divider()

st.caption("Người tạo ứng dụng: [Đỗ Bích Vân]] | MSSV: [037308002902]")
