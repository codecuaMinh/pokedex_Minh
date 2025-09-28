from graphviz import Digraph

# Helper to add labeled edge
def add_edge(graph, src, dst, label=None):
    if label:
        graph.edge(src, dst, label)
    else:
        graph.edge(src, dst)

# Activity diagram for UC07 (Nghỉ phép)
uc07 = Digraph("UC07_Leave", format="png")
uc07.attr(rankdir="TB", size="6")

uc07.node("start", "Bắt đầu", shape="circle")
uc07.node("nv_create", "Nhân viên tạo đơn nghỉ", shape="box")
uc07.node("check_quota", "Hệ thống kiểm tra quota", shape="diamond")
uc07.node("quota_ok", "Đủ quota", shape="box")
uc07.node("quota_fail", "Hết quota / trùng lịch", shape="box")
uc07.node("send_manager", "Gửi quản lý duyệt", shape="box")
uc07.node("approve?", "Quản lý duyệt?", shape="diamond")
uc07.node("approved", "Duyệt: Trừ quota, lưu", shape="box")
uc07.node("rejected", "Từ chối, lưu", shape="box")
uc07.node("end", "Kết thúc", shape="circle")

add_edge(uc07,"start","nv_create")
add_edge(uc07,"nv_create","check_quota")
add_edge(uc07,"check_quota","quota_ok","Yes")
add_edge(uc07,"check_quota","quota_fail","No")
add_edge(uc07,"quota_ok","send_manager")
add_edge(uc07,"send_manager","approve?")
add_edge(uc07,"approve?","approved","Yes")
add_edge(uc07,"approve?","rejected","No")
add_edge(uc07,"approved","end")
add_edge(uc07,"rejected","end")
add_edge(uc07,"quota_fail","end")

uc07_path = "/mnt/data/UC07_Leave.png"
uc07.render(uc07_path, format="png", cleanup=True)

# Activity diagram for UC08 (Tính lương)
uc08 = Digraph("UC08_Payroll", format="png")
uc08.attr(rankdir="TB", size="6")

uc08.node("start", "Bắt đầu", shape="circle")
uc08.node("config", "QL cấu hình công thức", shape="box")
uc08.node("run", "Đến kỳ lương: QL chạy lương", shape="box")
uc08.node("calc", "Hệ thống tính toán & sinh bảng lương", shape="box")
uc08.node("review", "QL kiểm tra bảng lương", shape="box")
uc08.node("lock?", "Khóa lương?", shape="diamond")
uc08.node("locked", "Khóa bảng lương", shape="box")
uc08.node("publish", "Phát hành phiếu lương", shape="box")
uc08.node("emp_view", "Nhân viên đăng nhập xem phiếu", shape="box")
uc08.node("end", "Kết thúc", shape="circle")

add_edge(uc08,"start","config")
add_edge(uc08,"config","run")
add_edge(uc08,"run","calc")
add_edge(uc08,"calc","review")
add_edge(uc08,"review","lock?")
add_edge(uc08,"lock?","locked","Yes")
add_edge(uc08,"locked","publish")
add_edge(uc08,"publish","emp_view")
add_edge(uc08,"emp_view","end")
add_edge(uc08,"lock?","review","No")

uc08_path = "/mnt/data/UC08_Payroll.png"
uc08.render(uc08_path, format="png", cleanup=True)

(uc07_path, uc08_path)
