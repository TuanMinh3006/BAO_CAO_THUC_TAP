# BAO_CAO_THUC_TAP
## Tuần 1: Nền tảng cơ bản
### Python
### SQL cơ bản
#### Gồm 4 loại : DDL,DML,DCL,TCL
* DDL(Data Definition Language): định nghĩa cấu trúc CSDL(CREATE,DROP,ALTER)
* DML(Data Manipulation Language): Thao tác dữ liệu(SELECT, INSERT ,UPDATE, DELETE)
* DCL(Data control Language): quản lý quyền truy cập(Grant, Revoke)
* TCL(Transaction Control Language): quản lý giao dịch (COMMIT, ROLLBACK)
   -  COMMIT: lưu vĩnh viễn tất cả các thay đổi được thực hiện trong giao dịch vào CSDL
   -  ROLLBACK: Hủy bỏ tất cả các thay đổi trong giao dịch, đưa cơ sở dữ liệu về trạng thái trước khi giao dịch bắt đầu.
### Linux command line: Các câu lệnh cơ bản trong shell
#### Câu lệnh lấy thông tin:
  * Whoami: lấy tên username
  * Id: userID và group ID
  * Uname: tên operation system
  * Ps: kiểm tra tiến trình
#### Làm việc với file:
  * Cp: copy file
  * Mv: đổi tên và đường dẫn của file
  * Rm: xóa file
  * Touch : tạo file trống và cập nhật file timestamp
  * Chmod: đổi quyền file
  * Wc: đếm dòng, ký tự trong file
  * Grep: tìm kiếm 
#### Làm việc với directories
  * Ls: liệt kê file và dir
  * Find: tìm file trong dir tree
  * Pwd: lấy đường dẫn hiện tại
  * Mkdir: tạo dir
  * Cd : chuyển thư mục làm việc(cd .. : trở về thư viện parent)
  * Rmdir: xóa dir
#### In file và nội dung file:
* Cat: in ra nội dung file
* More: in ra nội dung file từng trang một
* Head: in ra N dòng đầu tiên trong file
* Tail: in ra N dòng cuối cùng trong dile
* Echo: in ra string và biến

#### Nén và giải nén:
* Tar: lưu trữ 1 file 
* Zip: nén 1 tệp file
* Unzip:giải nén 1 tệp file

#### Networking:
* hostname: in ra hostname
* ping: gửi package to URL và in phản hồi
* ifconfig: hiển thị và cấu hình system network 
* curl: đọc nội dung 
* wget: download file từ URL
### MySQL
#### MySQL là một hệ quản trị cơ sở dữ liệu quan hệ (RDBMS - Relational Database Management System) mã nguồn mở, được sử dụng rộng rãi trong các ứng dụng web và doanh nghiệp. MySQL được phát triển bởi Oracle Corporation và nổi tiếng với tốc độ, độ tin cậy, và tính dễ sử dụng. Nó hỗ trợ chuẩn SQL và được sử dụng trong nhiều ứng dụng như WordPress, Drupal, và các hệ thống thương mại điện tử.
#### Đặc điểm chính là:
* Mã nguồn mở
* Hiệu suất cao: Tối ưu cho các ứng dụng yêu cầu truy vấn nhanh và khối lượng dữ liệu lớn
* Đa nền tảng: có thể chạy trên nhiều hệ điều hành khác nhau
#### Các cài đặt trên Linux 
* Cập nhật apt
   -  sudo apt-get update
   -  sudo apt update
* Cài MySQL
  - sudo apt install mysql_server
* Check version
   - MySQL --version
 * Check status
   -  sudo systemctl status MySQL
 * Vào MySQL
   - sudo MySQL -u root
  * Thoát
    - Exit
#### Tệp cấu hình thường nằm ở /etc/mysql/my.cnf và 1 số thông số quan trọng:
* Bind-address: quy định địa chỉ IP mà Mysql lắng nghe
* Max_connections: số lượng connect đồng thời tối đa
## Tuần 2: Kiến trúc dữ liệu
### Khái niệm OLTP vs OLAP 
#### OLTP(Online Transaction Processing):
* Xử lý các giao dịch trực tuyến realtime, tập trung vào các hoạt động hàng ngày như thêm , sửa, xóa dữ liệu.
* Đặc điểm:
   - Dữ liệu: giao dịch ngắn, thường xuyên liên quan den một lượng nhỏ dữ liệu.
   - Tính chất: cập nhật thường xuyên, yêu cầu tốc dộ cao, xử lý đồng thời nhiều user
   - Cấu trúc dữ liệu: Dữ liệu sẽ được chuẩn hóa theo các chuẩn NF để tránh dữ liệu dư thừa, thường ở trong CSDL
   -  Ví dụ: hệ thống bán hàng POS, quản lý ngân hàng, đặt vé trực tuyến
   -  Truy vấn: Đơn giản, cập nhật số dư tk,…
   -  Hiệu suất: tối ưu cho các thao tác write và read nhanh trên dữ liệu nhỏ
#### OLAP(Online Analytical processing): 
* Mục đích: phân tích dữ liệu để hỗ trợ ra quyết định, thường dùng cho báo cáo và phân tích kinh doanh.
* Đặc điểm:
   - Dữ liệu: Xử lý khối dữ liệu lớn, thường là dữ liệu lịch sử được tổng hợp
   - Tính chất: Truy vấn phức tạp, đọc nhiều, ít cập nhật
   - Cấu trúc : Dữ liệu phi chuẩn hóa, thường lưu trong data warehouse với mô hình star schema hoặc snowflake schema
   - Ví dụ: Báo cáo doanh thu, phân tích xu hướng, dự báo kinh doanh
   - Truy vấn: Phức tạp.Ví dụ: “Tổng hợp doanh thu theo khu vực trong 5 năm”
   - Hiệu suất: Tối ưu cho việc đọc và tổng hợp dữ liệu
### NGUYÊN TẮC THIẾT KẾ DB
#### Dành cho OLTP:
* Được tổ chức thành các bảng db để đảm bải tính dư thừa và đảm bảo tính toàn vẹn, thường áp dụng đến dạng chuẩn 3NF
* Tối ưu hóa giao dịch: Schema được thiết kế để hỗ trợ các thao tác đọc ghi nhanh trên các tập dữ liệu nhỏ
* Sử dụng khóa chính và khóa ngoại
* Index : sử dụng index để tăng tốc truy vấn, nhưng cần lưu ý nhiều index quá có thể làm chậm thao tác ghi
#### Dành cho OLAP:
* Phi chuẩn hóa: Dữ liệu được tổ chức để giảm số lượng phép join và tăng tốc truy vấn. Thường được sử dụng mô hình star schema hoặc snowflake schema
* Tập trung vào truy vấn đọc
* Dùng bảng Fact và Dimension:
•	Fact Table: Lưu trữ số liệu định dạng (metrics), ví dự như: doanh thu, số lượng bán
•	Dimension Table: Lưu trữ thông tin mô tả(context), ví dự như thời gian, khách hàng, sản phẩm
* Hiệu suất truy vấn: sử dụng các kĩ thuật như phân vùng, chỉ mục bitmap, hoặc vật lý hóa để tối ưu truy vấn
### CAP Theorem(Định lý CAP): 
#### Được gọi là định lý brewer, là một nguyên lý cơ bản trong hệ thống phân tán(distributed system), mô tả sự đánh đổi giữa 3 đặc tính quan trong của 1 hệ thống cơ sở dữ liệu phân tán.Nó cho biết 1 hệ thống phân tán chỉ có thể đảm bảo tối đa 2 trong 3 đặc tính sau cùng 1 lúc:
#### Ba đặc tính của CAP:
* Consistency(Tính nhất quán)
   - Mọi node trong hệ thống đều thấy cùng một dữ liệu tại cùng một thời điểm.
* Availability(Tính sẵn sàng):
   - Hệ thống luôn phản hồi các yêu cầu(read hoặc write) từ client, ngay cả khi có lỗi xảy ra(như mất kết nối hoặc lỗi node)
* Partition tolerance(khả năng chịu lỗi phân vùng)
   - Hệ thống tiếp tục hoạt động ngay cả khi có sự cố phân vùng mạng(network partition), tức là các node không thể giao tiếp với nhau do mất kết nối.
   - Vì các hệ thống phân tán thường chạy trên nhiều máy chủ, phân vùng mạng là điều không thể tránh khoirm nên hầu hết các hệ thống phải được thiết kế để chịu lỗi phân vùng.
* NOTE:
   - Thường các hệ thống thường phải hi sinh 1 trong tính consistency hoặc tính Availability . vì đa số tính Partition Tolerance là tính bắt buộc của 1 hệ thống phân tán.Còn các hệ thống ưu tiên CS thì thường lưu trữ trên CSDL không phân tán (1 node)
   - OLAP : Thường ưu tiên CA
   - OLAP: thường ưu tiên AP vì data warehouse thường phân tán trên nhiều nút để xử lý data lớn.
   - Không thể  đạt được cả 3 tính cùng 1 lúc vì:
      - Để đảm bảo tính Consistency: Hệ thống phải đảm bảo rắng all các nút đều thấy dữ liệu.Nếu có phân vùng mạng nào mà node không cập nhật đc thông tin mới nhất thì hệ thống sẽ cô lập các node đó khỏi các yêu cầu(read/write) để có thể đảm bảo tính.
      - Đảm bảo tính  Availability: Hệ thống phải phản hồi mọi yêu cầu, ngay cả khi có lỗi phân vùng mạng. Điều này khiến cho việc các node trả về có thể là data cũ hoặc chưa đồng bộ => dẫn tới mất tính Consistency.
#### CAP trong NOSQL
* NoSQL được thiết kế để đáp ứng các ứng dụng hiện đại với yêu cầu về khả năng mở rộng, hiệu suất cao, và xử lý dữ liệu lớn và được thiết kế cho môi trường phân tán. Vậy nên Partition Tolerance là bắt buộc trong các hệ thống phân tán
* Các hệ thống NoSQL thường được thiết kế ưu tiên một trong hai mô hình:
   - CP (Consistency + Partition Tolerance): Ưu tiên tính nhất quán và chịu đựng phân vùng, nhưng có thể hy sinh tính khả dụng. Ví dụ: Nếu có phân vùng mạng, hệ thống có thể từ chối một số yêu cầu để đảm bảo dữ liệu nhất quán. Các CSDL như MongoDB (ở chế độ nhất quán cao) hoặc HBase thường thuộc nhóm này.
   - AP (Availability + Partition Tolerance): Ưu tiên tính khả dụng và chịu đựng phân vùng, nhưng có thể trả về dữ liệu không nhất quán tạm thời (eventual consistency). Ví dụ: Cassandra hoặc DynamoDB thường thuộc nhóm này.
* Ứng dụng trong NoSQL
   - Cassandra: Ưu tiên AP, cung cấp tính khả dụng cao và eventual consistency, phù hợp cho các ứng dụng cần xử lý khối lượng lớn yêu cầu mà không cần nhất quán tức thời.
   - MongoDB: Có thể cấu hình để ưu tiên CP hoặc AP, tùy thuộc vào yêu cầu về tính nhất quán của ứng dụng.
   - Redis: Thường ưu tiên tính khả dụng và hiệu suất, nhưng có thể không đảm bảo tính nhất quán mạnh trong một số trường hợp phân vùng.
### ACID và BASE 
#### ACID: Atomicity,Consistency,isolation,Durability  là các tập hợp bảo đảm tính toàn vẹn của giao dịch trong CSDL
* A.Atomicity (Tính nguyên tử): Đảm bảo rằng một giao dịch được thực hiện hoàn toàn hoặc không thực hiện gì cả. Nếu bất kỳ phần nào của giao dịch thất bại, toàn bộ giao dịch sẽ bị hủy bỏ (rollback)
* B.Consistency (Tính nhất quán): Đảm bảo rằng sau một giao dịch đưa có sở dữ liệu từ trạng thái hợp lệ sang trạng thái hợp lệ khác , tuân thủ các rang buộc, quy tắc và tính toàn vẹn mà dữ liệu đã được định nghĩa sẵn(như khóa chính, khóa ngoại, rang buộc,…)
   - Ví dụ như: Ô A có 500k tiền trong tài khoản và ô C có 300k tiền trong tài khoản. Tổng số tiền là 800k. Thì tính nhất quán ở đây để bảo đảm toàn vẹn là: nếu ô A chuyển cho ông C 100k thì cả 2 ô đều phải có 400k và tổng số tiền của 2 ô bắt buộc phải là 800k.
* C.Isolation(Tính cô lập): Các giao dịch được thực hiện độc lập với nhau. Một giao dịch chưa hoàn thành(uncommitted) thì sẽ không ảnh hưởng tới các giao dịch khác.
* D.Durability(Tính bền vững): Đảm bảo rằng khi một giao dịch đã được xác nhận(đã committed) thì nó sẽ được lưu trữ vĩnh viễn, ngay cả khi hệ thống gặp sự cố.
* ACID thường dùng cho hệ thống yêu cầu độ chính xác cao như ngân hàng, tài chính,…
#### BASE: Basically available, soft sate, eventually consistent
* Basically available (Cơ bản sẵn sàng): Hệ thống đảm bảo tính sẵn sàng cao, nghĩa là người dùng hầu như luôn nhận được phản hồi, ngay cả khi một số node của hệ thống bị lỗi. Tuy nhiên, dữ liệu trả về có thể không phải là mới nhất.
* Soft state(Trạng thái mềm): Dữ liệu trong hệ thống có thể thay đổi theo thời gian mà không cần giao dịch rõ rang. Hệ thống không đẩm bảo trạng thái dữ liệu luôn nhất quán tại 1 time.
* Eventually consistency(Nhất quán cuối cùng): Hệ thống đảm bảo rằng nếu không có cập nhật mới nhất, thì tất cả các nút trong hệ thống cuối cùng sẽ đạt được trạng thái nhất quán.
* BASE thường được sử dụng trong các hệ thống phân tán, nơi khả năng yêu cầu mở rộng (scalability) và hiệu suất cao, như mạng xã hội, hệ thống thương mại điện tử hoặc các ứng dụng thời gian thực.
### ETL vs ELT
#### ETL: Extract – Transform- Load
* Chuyển đổi được thực hiện trước khi dữ liệu được load
* Phù hợp với các hệ thống kho dữ liệu truyền thống(on-premises) như SQL Server, oracle
* Thích hợp khi cần đảm bảo dữ liệu đã được xử lý hoàn toàn trước khi lưu trữ
* Các trường hợp sử dụng ETL pipeline:
   - Chuyển data từ OLAP->OLTP
   - Làm Dashboard, bảng báo cáo
   - Phù hợp với hệ thống data warehouse
* Ưu điểm:
   - Dữ liệu sẽ được nhất quản trước khi đưa vào lưu trữ
   - Giảm tải cho hệ thống đích vì dữ liệu đã được tối ưu hóa
* Nhược điểm:
   - Tốn ít thời gian và tài nguyên ở bước chuyển đổi và đặc biệt là đối với khối lượng dữ liệu lớn
   - Ít linh hoạt khi cần thay đổi quy trình chuyển đổi sau khi dữ liệu đã được tải
#### ELT: Extract-Load-Transform
* Chuyển đổi được thực hiện sau khi dữ liệu đã được tải vào kho dữ liệu
* Thích hợp cho dữ liệu thô, khối lượng lớn hoặc khi cần xử lý dữ liệu theo real-time
* Các trường hợp sử dụng:
   - Yêu cầu khả năng mở rộng của bigdata
   - Phân tích theo realtime trên streaming
   - Trích xuất data từ nhiều nguồn
* Ưu điểm:
   - Nhanh hơn ở giai đoạn load vì không cẩn chuyển đổi trước.
   - Linh hoạt hơn, dễ dàng thay đổi logic chuyển đổi sau khi dữ liệu đã được tải.
* Nhược điểm:
   - Dữ liệu thô có  thể chiếm nhiều không gian lưu trữ hơn trước khi chuyển đổi.
#### Schema Snowflake vs Schema Star:
##### Schema Star:
* Star là 1 kiểu cơ sở dữ liệu gồm 1 bảng Fact(bảng sự kiện) và nhiều bảng Dimension(bảng chiều)
*  Bảng Fact là bản trung tâm của schema star, chứa các số liệu định lượng hoặc các sự kiên cần phân tích.Gồm khóa ngoại và các cột số liệu,…
*  Bảng Dimension: lưu trữ thông tin mô tả liên quan đến các khía cạnh của dữ liệu.Mỗi bảng chứa  1 khóa chính liên kết với khóa ngoại trong bảng Fact
*  Ưu điểm:
   - Hiệu suất truy vấn cao: do dữ liệu không chuẩn hóa, các truy vấn thường nhanh hơn vì ít phải thực hiện phép nối phức tạp.
   - Dễ hiêu và sử dụng: cấu trúc đơn giản
* Nhược điểm:
   - Dư thừa dữ liệu: do không được chuẩn hóa, dữ liệu có thể lặp lại trong các bảng dimension, dẫn đến tang kích thước lưu trữ.
##### Schema Snowflake
* Là một biến thể của schema star, trong đó các bảng dimension được chuẩn hóa thành nhiều bảng liên quan, tạo ra cấu trúc phức tạp hơn, giống hình bông tuyết.=> khiến cho schema Snowflake tạo ra nhiều lớp bảng hơn so với schema star.
* Ưu điểm:
   - Tiết kiệm không gian lưu trữ: do dữ liệu được chuẩn hóa, tránh lặp lại thông tin
   - Dễ bảo trì và mở rộng: phù hợp với các hệ thống có dữ liệu phức tạp, nhiều mối quan hệ
   - Phù hợp với các hệ thống lớn: khi kho dữ liệu có nhiều chiều và mối quan hệ phức tạp, schema snow dễ quản lý hơn
* Nhược điểm:
   - Truy vấn phức tạp hơn: do có nhiều bảng và phép nối, các truy vấn SQL phức tạp hơn và có thể chậm hơn so với schema star.
   - Hiệu suất thấp hơn so với star snow vì phải join nhiều bảng
## Tuần 3: BigData - Batch Processing
### Apache Spark (RDD, DataFrame)
#### Apache Spark là một hệ thống xử lý phân tán mã nguồn mở, được phát triển để xử lý khối lượng cộng việc dữ liệu lớn một cách hiệu quả.Apache nổi bật ở khả năng ghi vào bộ nhớ đệm trong bộ nhớ và thực thi các truy vấn tối ưu hóa, giúp cho tối ưu hóa việc phân tích dữ liệu.
#### Spark gồm các thành phần chính sau:
* Spark Core: thành phần cốt lõi, chịu trách nhiệm quản lý bộ nhớ, lịch trình, và tương tác với các hệ thống lưu trữ
* Spark SQL: Hỗ trợ truy vấn dữ liệu tương tác với tốc độ nhanh và độ trễ thấp
* Spark streaming: Cung cấp khả năng phân tích dữ liệu thời gian thực
* Mlib: thư viện máy học, hỗ trợ thực hiện các thuật toán máy học trên quy mô lớn
* GraphX: khung xử lý đồ thị phân tán, giúp người dùng thực hiện các bài toán liên quan đến đồ thị.
#### RDD (resilient distributed dataset):
* RDD chia phân vùng và xử lý các phân vùng đó song song và cùng 1 lúc luôn.
* Các loại thao tác làm việc với RDD: transformations(biến đổi) và actions(hành động).
   - Transformation (Phần lệnh):
     - Map: áp dụng 1 hàm lên từng phần tử trong Dataframe/RDD và trả về một DataFrame/RDD mới với các phần tử đã được biến đổi.
     - Filter: Lọc các phần tử trong DataFrame/RDD thỏa mãn 1 điều kiện nhất định.
     - flatMap: Áp dụng một hàm lên từng phần tử trong RDD và “Làm phẳng” kết quả để tạo ra 1 RDD mới(tức là loại bỏ cấu trúc lồng nhau)
     - distinct: Loại bỏ các phần tử trùng lặp trong DataFrame/RDD, trả về tập dữ liệu với các giá trị duy nhất
     - union:Kết hợp 2 dataframe/RDD thành 1 Datafram/RDD duy nhất , giữ nguyên tất cả các bản ghi(bao gồm cả trùng lặp)
     - join:Kết hợp 2 DataFrame dựa trên một điều kiện chung(cột khóa), tương tự phép nối trong SQL
     - groupBy:Nhóm các bản ghi trong DataFrame theo một hoặc nhiều cột, thường kết hợp các hàm tổng hợp như count,sum,avg,…
   - Action (Phần thực thi các lệnh):
      - collect: Thu thập toàn bộ dữ liệu từ RDD hoặc Dataframe và trả về dưới dạng 1 mảng array hoặc danh sách list tại driver node
      - take: Lấy n phần tử đầu tiên từ RDD hoặc Dataframe và trả về dưới dạng mảng tại driver
      - count: đếm tổng số bản ghi(row) trong RDD hoặc DataFrame
      - reduce: Áp dụng một hàm giảm(reduction dunction) để gộp các phần tử trong RDD thành 1 giá trị duy nhất.
      - saveAsTextfile: Lưu dữ liệu từ RDD(hoặc DataFrame sau khi chuyển sang RDD) thành các file văn bản trong một thư mực được chỉ định.
   - RDD có tính không thể thay đổi: 1 khi RDD đã khởi tạo thì không thể thay đổi được.
#### DataFrame
* Trong Apache Spark, DataFrame là một cấu trúc dữ liệu phân tán, được tổ chức theo dạng bảng với các cột có tên và kiểu dữ liệu, tương tự như bảng trong CSDL trong Pandas(Python). Nó là một phần quan trọng của Spark SQL, được thiết kế để xử lý dữ liệu (bigdata) một cách hiệu quả trên hệ thống phân tán. Trong các hàng và các cột:
   - Mỗi cột có một tên và một kiểu dữ liệu cụ thể (Ví dụ: String, Integer, Double, ...)
   - Dữ liệu được phân tán trên nhiều node trong 1 cụm spark, cho phép xử lý // và mở rộng quy mô
* Là một abstraction cấp cao so với RDD
#### Dataset
* Dataset là một một cấu trúc dữ liệu cấp cao trong Spark, kết hợp lợi ích của RDD (kiểm soát mạnh mẽ) và DataFrame (tối ưu hóa hiệu suất). Dataset là một tập hợp phân tán các đối tượng được định kiểu (strongly-typed) theo một schema.
* Đặc điểm:
   - Chỉ có trong Scala và Java: Dataset không được hỗ trợ trực tiếp trong Python hoặc R (trong Python, DataFrame tương đương với Dataset không định kiểu).
   - Kiểm tra kiểu tĩnh: Dataset yêu cầu định nghĩa kiểu dữ liệu cụ thể (ví dụ: Dataset[Person]), giúp phát hiện lỗi sớm trong quá trình biên dịch.
   - Hiệu suất cao: Tương tự DataFrame, Dataset được hưởng lợi từ Catalyst Optimizer và mã hóa Tungsten để tối ưu hóa bộ nhớ và CPU.
   - Linh hoạt hơn DataFrame: Dataset hỗ trợ các phép biến đổi hàm (functional transformations) giống RDD, nhưng vẫn giữ được lợi ích của DataFrame.

#### So Sánh RDD với DataFrame và Dataset: 
|Tiêu chí          | RDD                               | DataFrame                          | Dataset                             |
|------------------|-----------------------------------|------------------------------------|-------------------------------------|
|Cấp độ            |Cấp thấp                           |  Cấp cao                           |   Cấp cao                           |
|Schema            | Không có                          |   Có (cột có tên, kiểu dữ liệu)    |    Có, schema rõ ràng và type-safe    |
|Hiệu suất         | Thấp hơn, cần tối ưu thủ công     |   Cao (Catalyst, Tungsten)         |    Cao (Catalyst, Tungsten)         |
|Hỗ trợ SQL        | Có, tích hợp chặt chẽ với SparkSQL|   Không hỗ trợ trực tiếp SQL       |    Có hỗ trợ SQL                    |
|Ngôn ngữ hỗ trợ   | Python, Scala, Java, R            |   Python, Scala, Java, R           |    Chỉ Scala, Java                  |
|Tính linh hoạt    | Rất linh hoạt                     |   Ít linh hoạt hơn RDD             |    Linh hoạt hơn DataFrame          |
|Dễ sử dụng        | Khó, cần viết nhiều code          |   Dễ, giống SQL                    |    Dễ, kết hợp SQL và hàm           |
|Ứng dụng          | Dữ liệu không cấu trúc            |  Dữ liệu có cấu trúc               |  Dữ liệu có cấu trúc + lập trình hàm|

* NOTE: 
   - Catalyst là bộ tối ưu hóa truy vấn (query optimizer) của Spark SQL và DataFrame API. Nó được giới thiệu từ Spark 1.2 và là một phần cốt lõi của Spark, sử dụng ngôn ngữ lập trình Scala để xây dựng một optimizer linh hoạt, có thể mở rộng.Lợi ích: Giúp truy vấn nhanh hơn, tiết kiệm tài nguyên (CPU, memory), đặc biệt với dataset lớn từ các nguồn như Parquet, Hive, hoặc JDBC. Ví dụ, nếu dataset của bạn có hàng triệu dòng, Catalyst có thể giảm dữ liệu đọc từ đĩa bằng cách chỉ tải những phần cần thiết.
   - Tungsten (hay Project Tungsten) là engine thực thi (execution engine) của Spark, được giới thiệu từ Spark 1.5. Nó tập trung vào tối ưu hóa ở lớp vật lý (physical layer), cải thiện hiệu suất CPU và memory bằng cách tận dụng phần cứng tốt hơn. Tungsten làm việc chặt chẽ với Catalyst: Catalyst tạo kế hoạch logic, còn Tungsten thực thi kế hoạch đó một cách hiệu quả.Lợi ích: Tăng tốc độ xử lý dataset lên 2-10 lần, đặc biệt trên cluster lớn, bằng cách giảm lãng phí CPU và memory. Nó không áp dụng cho RDD (Resilient Distributed Datasets) mà chủ yếu cho DataFrame/SQL.
   - Type_safe trong schema là Spark đảm bảo rằng các thao tác bạn thực hiện trên Dataset (như truy cập cột, xử lý dữ liệu) được kiểm tra kiểu dữ liệu ngay tại thời điểm biên dịch (compile-time, lúc chương trình được kiểm tra cú pháp, kiểu dữ liệu, và các quy tắc của ngôn ngữ lập trình), thay vì chỉ phát hiện lỗi tại thời điểm chạy (runtime, Đây là lúc mã thực sự được chạy, dữ liệu được xử lý, và các kết quả được tạo ra trên máy tính hoặc máy ảo).
### Hadoop HDFS
#### Hadoop ecosystem là 1 hệ sinh thái gồm nhiều thành phần kết hợp lẫn nhau để hỗ trợ xử lý dữ liệu lớn:
* Các phần mềm sẽ sử dụng cho từng giai đoạn:
   - Nhập dữ liệu:flume,sqoop
   - Chứa data: HDFS, HBase
   - Xử lý và phân tích: Pig,Hive
   - Truy cập dữ liệu: Hue
#### HDFS:
*  Là một hệ thống tệp tin được phân phối trên nhiều máy chủ tập tin, cho phép lập trình viên truy cập, lưu trữ các tập tin từ bất kì mạng hay máy tính nào.
*  Là lớp lưu trữ của Hadoop
*  Cách hoạt động: Chia các file thành các block -> tạo bản sao (replication) của các block-> lưu các block ở các máy khác nhau.
*  Một số khái niệm cơ bản:
   - Block(Khối): khối lượng tối thiểu có thể đọc và viết. Size: 64->128 MB.
   - Node: Là hệ thống duy nhất chịu trách nhiệm và xử lý dữ liệu.
   - Có 2 loại Node: Primary node(Master Node) và secondary Node(Data Node)
        - Namenode: là node chính, chịu trách nhiệm quản lý metadata của hệ thống tệp, bao gồm thông tin về cấu trúc thư mục, vị trí tệp và vị trí của các bản sao dữ liệu.Như một quản trị viên để theo dõi và phối hợp với các Datanode
        - DataNode: là các node chứa dữ liệu thực tế, chịu trách nhiệm lưu trữ và truy xuất các data blocks theo sự điều phối của Name node.
   - Note: HDFS có cơ chế viết 1 lần và đọc nhiều lần. Mỗi tệp chỉ được ghi 1 lần sau khi khởi tạo và sau đó không được sửa đổi. Nếu muốn cập nhật thì dữ liệu sẽ được ghi dưới 1 tệp mới.

### Parquet/ORC
#### Parquet
* Apache parquet: là 1 định dạng cột có sẵn cho bất kì project nào của Hadoop. Nó được thiết kế để hiệu quả và hiệu suất giúp tối ưu hơn các truy vấn phức tạp trên các bộ dữ liệu lớn.
* Ưu điểm:
   - Vì lưu trữ theo cột nên giúp tối ưu hóa việc đọc/ ghi trên đĩa và nén dữ liệu hiệu quả hơn. Giảm lượng dữ liệu truyền từ đĩa sang bộ nhớ, dẫn đến hiệu suất truy vấn nhanh hơn. Vì lưu theo kiểu dạng cột nên khi 1 truy vấn chỉ cần dữ liệu từ 2 cột trong 100 cột của tệp dữ liệu thì parquet chỉ lấy dữ liệu từ 2 cột đó, giảm thiểu thao tác đọc/ghi trên đĩa. Ngược lại nếu lưu trữ theo trên row thì khi đọc cần phải đọc lại toàn bộ hàng baoa gồm cả các dữ liệu không cần thiết, gây tốn tài nguyên I/O.
   - Việc đọc chọn lọc này giảm lượng dữ liệu truyền từ đĩa sang bộ nhớ, giúp tăng tốc độ thực thi truy vấn, đặc biệt với các tác vụ phân tích trong  kho dữ liệu
   - Parquet hỗ trợ các cấu trúc dữ liệu lồng ghép phức tạp, cho phép thay đổi cách tổ chức dữ liệu.
   - Parquet hỗ trợ nén và mã hóa => giúp giảm bộ nhớ và cải thiện performance
* Nhược điểm:
   - Bởi vì parquet nén và mã hóa theo dạng cột nên, chi phí cho việc ghi dữ liệu khá cao
   - Không phù hợp với dữ liệu nhỏ bởi vì các ưu điểm của việc lưu theo cột không được phát huy hết mức.
#### ORC: Optimized row columnar
* Là kiểu định dạng file khác được sử dụng trong hệ thống Hadoop. Cũng được lưu trữ theo dạng column.
* Ưu điểm của ORC: 
   - Nén: ORC cung cấp tốc độ nén ấn tượng hơn parquet. Nó cũng bao gồm các chỉ mục nhẹ được lưu trữ trong tệp, giúp cải thiện hiệu suất đọc
   - Hỗ trợ các loại phức tạp, bao gồm các structs,lists,maps và union types
   - Hỗ trợ rất tốt cho các ACID transactions trong Hive, cũng cấp các tính năng như update, delete, và merge.
* Nhược điểm:
   - Cộng đồng hỗ trợ ít
   - Chi phí viết cao

#### Bảng so sánh giữa ORC và Parquet


|                          |     Parquet                                                     |                           ORC                                                        |
---------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------------|
|Kiểu chứa dữ liệu         | Dạng cột                                                        |              Dạng cột                                                                |             
|   Schema                 | Hỗ trợ các schema phức tạp và lồng nhau                         |      Hỗ trợ các dạng schema phức tạp nhưng ít linh hoạt hơn đối với schema lồng nhau |
|ACIDTransactions|Ít hỗ trợ|Hộ trợ đầy đủ ACID transactions trong HIVE                       |
|Phù hợp với dữ liệu lớn   |Có                                                               |Có                                                                                    |
|Hiệu suất trong Analytics|Xuất sắc, đặc biệt với các tool như Apache Spark hoặc Apache Arrow|Tốt, phù hợp với các framewordks dựa trên HIVE                                        |


#### THỰC HÀNH LƯU TRỮ FILE DỮ LIỆU LÊN HADOOP BẰNG SPARK DƯỚI 2 DẠNG PARQUET VÀ ORC
#### FILE THỰC HIỆN: vnm_children_under_five_2020.csv(1.47GB)
#### BẢNG SO SÁNH
|                  |Parent             |ORC                  |
-------------------|-------------------|---------------------|
|Time lưu trữ      | 13.36s            |12.78s               |
|Time read         | 1.15 s            |2.33  s              |
|Time query        | 0.42 s            |1.35 s               |
|Block size lưu trữ|128MB              |      256MB          |

* **Nhận xét: **Đối với xử lý dữ liệu lớn, thì partquet vẫn là 1 kiểu dữ liệu tối ưu và hiệu suất hơn ORC khi dùng Spark
## Tuần 4: Real-time Streaming
### Apache Kafka
* Là một hệ thống publish-subcribe messaging system
* Mã nguồn mở, được thiết kế để xử lý luồng dữ liệu lớn với độ trễ thấp và khả năng mở rộng cao
* Kafka tổ chức data vào “Topics”. “Produce”(app để gửi data) đẩy “message” vào trong những topics và consumer (app đọc data) nhận chúng. 
#### Các thành phần chính của Apache Kafka
##### Kafka broker
*	Là một server của kafka để lưu trữ dữ liệu. Thông thường cụm kafka bao gồm nhiều broker làm việc cung nhau để cung cấp khả năng mở rông, chịu lỗi và tính high availability. Mỗi broker sẽ chịu trách nhiệm chứa và làm các việc liên quan tới "topic"
##### Producer
* Là nơi sẽ gửi các “messages” tới các “topic” của kafka. Nó sẽ push data vào trong hệ thống kafka. Producers sẽ quyết định rằng “message”  nên đi đến “Topic” nào
##### Kafka Topic
* Là các danh mục hoặc các kênh , nơi là dữ liệu được tổ chức thành các chủ đề “Topic”.
##### Consumers và consumer groups
* Là ứng dụng đọc message từ các topic kafka. 
* Các consumers thuộc một nhóm có thể đọc các topic tương tự nhau. Nhưng mỗi message phải được thực hiện bởi 1 consumers trong nhóm. Điều này giúp cân bằng tải và cho phép các “consumer” có thể đọc  message từ bất kỳ offset nào.
* Partitions: Cho phép bạn xử lý song song các topic bằng cách chia các data trong 1 topic qua nhiều brokers
##### Zookeeper
* Kafka dùng apache Zookeeper để quản lý metadata, kiểm soát access vào các tài nguyên Kafka.Zookeeper đảm bảo tính high availability bằng cách chắc chắn tằng cụm Kafka vẫn hoạt động ngay cả khi 1 broker lỗi.
##### Cách Kafka hoạt động :
###### Bước 1: Producers gửi data
* Producers sẽ tạo data và gửi nó vào kafka
* Data có thể bao gồm : logs, giao dịch, events,…
* Kafka chia dữ liệu thành các phần nhỏ gọi là partitons , giúp xử lý dễ dàng hơn khi xử lý dữ liệu lớn.
###### Bước 2: Kafka chứa dữ liệu
* Tổ chức data thành các “topic” (dữ liệu sẽ được lưu ở đây 1 khoản thời gian nhất định)
* Ngay sau khi consumer đọc data thì kafka sẽ xóa dữ liệu ngay lập tức
* Để tránh mất dữ liệu, kafka sẽ nhân bản và lưu dữ liệu vào 1 server khác
###### Bước 3: Consumer đọc dữ liệu
* Cosumer sẽ subscribe các topic và đọc các message
* Consumers có thể chọn nơi để bắt đầu đọc, mặc dù nó là message mới nhất hoặc điểm gần nhất
###### Bước 4: Kafka cân bằng tải
* Zookeeper giúp kafka quản lý server nào chịu trách nhiệm chứa và phân phối dữ liệu
* Nếu 1 server tự sub thì kafka sẽ tự động chuyển dữ liệu sang server khác
###### Bước 5: Dữ liệu đã đc xử lý và sử dụng
* Mỗi consumers nhận dữ liệu, nó có thể chứa ở database hoặc phân tích nó hoặc trigger các envens khác
* Kakfa có thể làm việc với các tool như apache Spark, Flink, Hadoop để phân tích sâu hơn
##### Các mô hình xử lý dữ liệu:
###### Event streaming
* Chức năng chính của kafka là event streaming, nơi mà:
* Producers : đẩy message tới các topic kafka
* Consumers: subscribe các topic và nhận message ngay khi nó tới.
###### Message Queue 
* Kafka có thể hoạt động gần như message queue bằng cách sử dụng consumer groups: 
* Khi nhiều consumers thuộc 1 group, kafka sẽ phân phối các message và đảm bảo rằng mỗi message chỉ được xử lý một lần 
* Cái này giúp cân bằng tải, giúp đảm bảo không có 1 consumer nào bị quá tải 
###### Batch Processing
* Kafka có thể xử lý batch processing, Message có thể chứa trong các topic kafka và sẽ xử lý sau
* Các công cụ như apache Spark hoặc Hadoop có thể đọc dữ liệu từ Kafka theo đợt và phân tích nó 
* Nhiều consumers có thể đọc các messae giống nhau và cho phép phân phối dữ liệu realtime
###### Hybrid Model (Real-Time + Batch Processing)
* Nó có hỗ trợ support cả real-time lẫn batch processing
* Nó có thể gửi dữ liệu ngay lập tức để phân tích real-time trong khi lưu trữ nó để xử lý hàng loạt sau đó
* Thường sử dụng Kafka Streams, Spark Streaming và FLink 
#### Spark Streaming
* Spark Streaming là một thành phần của Apache Spark, cho phép xử lý dữ liệu theo thời gian thực (real-time) bằng cách xử lý các luồng dữ liệu (data streams) theo từng lô nhỏ (micro-batches). Nó tích hợp với hệ sinh thái Spark, tận dụng khả năng xử lý dữ liệu phân tán và tính toán song song để phân tích các luồng dữ liệu lớn từ nhiều nguồn như Kafka, Flume, hoặc socket.
##### Đặc điểm chính:
* 	Xử lý micro-batch: Dữ liệu được thu thập và xử lý trong các khoảng thời gian ngắn (thường là vài giây), thay vì xử lý từng bản ghi riêng lẻ như các hệ thống streaming truyền thống.
* 	Tích hợp với Spark: Có thể sử dụng các API của Spark (như Spark SQL, MLlib) để phân tích dữ liệu streaming.
* 	Khả năng mở rộng: Hỗ trợ xử lý dữ liệu lớn với độ trễ thấp trên các cụm phân tán.
* 	Tính chịu lỗi: Dữ liệu được lưu trữ tạm thời trong bộ nhớ và có cơ chế khôi phục lỗi (fault tolerance) thông qua RDD (Resilient Distributed Dataset).
* 	DStream: Khái niệm cốt lõi, biểu diễn luồng dữ liệu như một chuỗi các RDD được xử lý liên tục.

##### Ứng dụng:
* 	Phân tích log thời gian thực.
* 	Xử lý dữ liệu từ cảm biến IoT.
* 	Giám sát và phân tích dữ liệu mạng xã hội.
* 	Xử lý sự kiện trong các ứng dụng tài chính.
### Lambda Architecture
### <img width="747" height="344" alt="Image" src="https://github.com/user-attachments/assets/9f8fe0e1-0e87-473c-8ec1-b6fb3c2f5c3e" />
#### Lambda là 1 trong 3 kiến trúc của bigdata . Bao gồm layer batch , stream, serving data cho người dùng cuối query.
#### Các layer chính: Gồm 3 layer chính trong Lambda Architecture: 
* Batch Layer (Cold process): Là lớp chứa dữ liệu thô đưa tơi và tính toàn để tạo các kết quả chính xác thường sử dụng các công cụ như Hadoop, Spark(Batch processing). Các quy trình sẽ xảy ra trong một khoảng time lâu dài(có thể vài phút hoặc tới hàng năm).
* Stream Layer (Hot process or Speed layer) : Lớp luồng hoạt động trên dữ liệu thời gian thực để bổ sung cho các chế độ xem batch . Nó nhận được dữ liệu đến từ các máy khách khác nhau và thực hiện các bản cập nhật gia tăng cho kết quả lớp batch và lưu trữ chúng trong cơ sở dữ liệu dữ liệu được xử lý.
* Serving layer: Là một máy chủ hoặc một bộ phận máy chủ xử lý đầu ra của các query khác nhau từ các mô-đun khác nhau (như mô-đun phân tích, mô-đun thông báo) bằng các sử dụng các kết quả được gửi từ các layer batch và stream
#### Các tool sử dụng trong kiến trúc Lambda 
* Apache Hadoop sử dụng để chứa data và tạo các cụm phân tán
* HDFS : dùng để quản lý dữ liệu bất biến trong batch layer
* Spark: sử dụng cho data streaming , xử lý đồ thị và quá trình data batch
* Apache Cassandra sử dụng để chứa view real-time
* Apache kafka : sử dụng để streaming data trong layer speed
* Apache Storm: sử dụng để  cho các nhiệm vụ layer speed
* Apache HBASE: sử dụng cho layer serving
#### Ưu điểm 
* Đây là sự cân bằng tốt giữa tốc độ, độ tin cậy, và khả năng mở rộng
* Layer batch giúp quản lý dữ liệu lịch sử với bộ lưu trữ phân tán, có khả năng chịu lỗi, đảm bảo khả năng xảy ra lỗi thấp ngay cả khi hệ thống gặp sự cố
* Layer Stream: quản lý dữ liệu real-time với phản hồi tức thì nhưng độ chính xác thấp hơn 1 chút.

#### Nhược Điểm 
* Phức tạp: Cần duy trì hai hệ thống riêng biệt (batch và streaming), dẫn đến chi phí phát triển và vận hành cao. 
* Trùng lặp mã: Logic xử lý thường phải được triển khai hai lần (cho batch và streaming), gây khó khăn trong bảo trì. 
* Độ trễ ở Batch Layer: Xử lý batch thường chậm hơn, không phù hợp cho các truy vấn cần phản hồi ngay lập tức.
### Kappa Architecture
#### Là 1 kiến trúc thiết kế dàng cho xử lý các real-time data streams. Loại bỏ các layer batch riêng biệt  và data sẽ được truyền dưới dạng stream (Luồng)
#### Trong Kappa Architecture
* Dữ liệu sẽ được thu thập như luồng từ các nguồn khác nhau 
* Các công cụ xử lý luồng (như Apache Kafka, Apache Flink hoặc Apache Samza) xử lý các phép biến đổi, tập hợp và tính toán dữ liệu thời gian thực liên tục.
* Kiến trúc xử lý cả dữ liệu mới và lịch sử một cách thống nhất, phát lại các sự kiện khi cần thiết để xử lý lại dữ liệu hoặc xử lý các lỗi.
#### Mô hình này cung cấp khả năng mở rộng, đơn giản và xử lý dữ liệu có độ trễ thấp, phù hợp với các ứng dụng yêu cầu real-time cao
#### Các thành phần chính : 
* Nguồn dữ liệu: Data sẽ được ingested từ các nguồn real-time như các thiết bị IOT, log các app,… Các luồng dữ liệu này sẽ liên tục chảy vào hệ thống
* Các công cụ sử lý luồng: Là thành phần quan trọng trong kiến trúc Kappa. Các công cụ như Apache Kafka, Apache Flink, Apache Samza xử lý các luồng data đến trong thời gian thực. Nó thực hiện các nhiệm vụ nhưu lọc, biến đổi, tổng hợp …. 
* Nơi chứa data: Kết quả xử lsy stream được ghi vào 1 hệ thống lưu trữ có thể mở rộng, bền như CSDL Noquery (HBase, Cassandra) hoặc các hệ thống tệp phân tán (HDFS hoặc S3). Lưu trữ này thường được thiết kế để xử lý dữ liệu lịch sử và có thể dùng lại khi cần.
* Layer Serving: phục vụ cho người dùng cuối hoặc hệ thống cuối. Cung cấp quyền truy cập vào các phân tích, dashboard và ứng dụng real-time dựa vào dữ liệu mới.
* Cơ chế tái xử lý/ phản hồi: Bởi vì ko có quá trình Batch nên Kappa Architecture phụ thuộc vào khả năng tái xử lý sự kiện. Nếu dữ liệu cần xử lý lại (do code thay đổi hoặc bugs,..), hệ thống sẽ xử lý lại từ đầu.
#### Ưu điểm
* Đơn giản hơn: Chỉ cần duy trì một hệ thống xử lý luồng, giảm chi phí phát triển và bảo trì.
* Mã thống nhất: Logic xử lý chỉ cần được viết một lần, áp dụng cho cả dữ liệu thời gian thực và lịch sử (bằng cách "phát lại" dữ liệu từ log).
* Dễ mở rộng: Dễ dàng tích hợp với các hệ thống lưu trữ log như Kafka, hỗ trợ xử lý dữ liệu lớn.
* Độ trễ thấp: Phù hợp với các ứng dụng cần phản hồi nhanh.
#### Nhược điểm
* Phụ thuộc vào hệ thống log: Yêu cầu một hệ thống lưu trữ log đáng tin cậy (như Kafka) với khả năng lưu trữ dữ liệu lâu dài.
* Khó xử lý dữ liệu lịch sử lớn: Nếu cần xử lý lại toàn bộ dữ liệu lịch sử, việc "phát lại" (replay) dữ liệu có thể tốn tài nguyên.
* Độ chính xác: Có thể không đạt độ chính xác cao như Batch Layer trong Lambda, đặc biệt nếu dữ liệu thô có lỗi.


## Tuần 5: Workflow & Inte
### Apache Airflow (DAGs, operators)
-  Là công cụ để lập lịch, quản lý, và giám sát các quy trình xử lý dữ liệu.Dùng để tự động hóa các quy trình xử lý dữ liệu phức tạp.
-  Là một công cụ điều phối luồng. Là nền tảng xây dựng và chạy luồng.
-  Một workflow thường được đại diện bởi 1  DAG
-  Kiến trúc của Airflow: 
   -  Scheduler (Bộ lập lịch): Chịu trách nhiệm lập lịch và quản lý việc thực thi các DAG.
      -  Scheduler liên thực quét thư mục DAG để phát hiện các DAG mới hoặc thay đổi
      -  Kiểm tra trạng thái của các task trong CSDL metadata và quyết định task nào sẵn sàng chạy
      -  Sử dụng các executor để phân phối tác vụ đến các worker
   -  Executor (Bộ thực thi)
      -  Quyết định các tác vụ được thực thi(Trên cùng máy hoặc phân tán)
      -  Executor nhận lệnh từ Scheduler và gửi các tác vụ đến các worker để thực thi. 
      -  Các loại excutor:
         -  sequentialExecutor: chạy các task tuần tự trên cùng 1 máy
         -  LocalExecutor: chạy nhiều tác vụ song song trên cùng 1 máy 
         -  CeleryExecutor: Phân phối tác vụ đến các worker qua hàng đợi như RabbitMQ hoặc Redis, phù hợp với hệ thống phân tán
         -  KubernetesExecutor: mỗi tác vụ chạy trong một pob Kubernetes riêng
   -  Worker (Công nhân)
      -  Thực thi các task được phân phối bởi executor
      -  Mỗi worker là một tiến trình(process) hoặc pob (trong Kubernets) thực hiện các câu lệnh được định nghĩa trong operator(như BashOperator, PythonOperator)
   -  Web Server (Máy chủ web)
      -  Cung cấp giao diện UI cho người dùng để giám sát và quản lý DAG, tác vụ, trạng thái thực thi
      -  Cho phép xem log, kích hoạt DAG, xóa các trạng thái tác vụ hoặc cấu hình hệ thống
   -  Metadata Database (Cơ sở dữ liệu metadata)
      -  Lưu trữ thông tin về DAG, trạng thái tác vụ, lịch sử thực thi, kết nối(connections), biến(variables) và cấu hình
      -  Là nơi lưu trữ trạng thái cảu các thành phần để đảm bảo tính nhất quán
   -  DAG Files (File DAG)
      -  Là các file Python chứa định nghĩa của DAG, bao gồm các tác vụ, phụ thuộc và lịch trình
      -  Được lưu trong thư mục dags_folder (mặc định là ~/airflow/dags)
-  Đặc điểm của Apache Airflow 
   -  Tạo workflow bằng script Puthon
   -  Có giao diện UI hữu ích 
   -  Không giới hạn quy mô pipeline 
   -  Opensource 
-  Nguyên tắc của apache Airflow : 
   -  Scalable: có thể sẵn sàng mở rộng
   -  Đa nhiệm: có thể chứa nhiều task đồng thời 
   -  Extensible : có thể mở rộng thư viện phù hợp với môi trường 

### DAGS
-  DAGS: directed Acyclic Graph: là một đồ thị có hướng không chu kỳ, mô tả tất cả các bước xử lý dữ liệu trong 1 quy trình.
-  Mỗi DAG được xác địng trong 1 file DAG, nó định nghĩa một quy trình xử lý dữ liệu, trong đó các nút là các tác vụ(tasks) và các cạnh là các phụ thuộc giữa các tác vụ
-  Các tác vụ trogn DAG thường được xử lý tuần tự hoặc song song theo một lịch được định sẵn
-  Thành phần của 1 DAG:
   -  Khai báo thư viện 
   -  Đối số DAG (DAG arguments)
   -  Định nghĩa DAG
   -  Định nghĩa task
   -  Task pipeline
-  Vòng đời của 1 trang thái task: 
   -  No status: tác vụ chưa được xếp hàng để thực hiện
   -  Scheduled: Bộ lập lịch đã xác định rằng các phụ thuộc của nhiệm vụ được đáp ứng và đã lên lịch cho nó chạy
   -  Removed: Tác vụ đã bị mất khỏi DAG kể từ khi bắt đầu chạy
   -  Upstream failed: “tác vụ ngược dòng” không thành công. (Tác vụ ngược dòng là các tác vụ nằm trước một tác vụ trong mối quan hệ phụ thuộc trong DAG.ví dụ A->B thì A là tác vụ ngược dòng của B)
   -  Queued: Nhiệm vụ đã giao cho executor và đang đợi 1 worker có sẵn để thực thi
   -  Running: tác vụ được chạy bởi một worker 
   -  Success: tác vụ chạy xong không có lỗi 
   -  Failed: Tác vụ có lỗi trong khi thực thi và không chạy được 
   -  Up for retry: Tác vụ không thành công nhưng vẫn còn các lần thử lại và sẽ được lên lịch lại.

### Task: 
-  Là một đơn vị cơ bản để thực hiện một công việc nhỏ trong quy trình xử lý dữ liệu. Mỗi task là một quy trình và có thể lập lịch thực hiện tùy theo các điều kiện cụ thể.Một Task trong Airflow có các thuộc tính và phương thức sau: 
   -  Task_id: định danh duy nhất của task trong DAG
   -  Owner: người sở hữu task
   -  Depends_on_past: xác định liệu task hiện tại có phụ thuộc vào kết quả của task trước đó không 
   -  Retries: số lần thử lại nếu task thất bại
   -  Retry_delay: khoảng time giữa các lần thử lại
   -  Start_date: thời gian bắt đầu 
   -  End_date: thời gian kết thúc
   -  Execution_timeout: thời gian tối đa cho phép để thực hiện task
   -  On_failure_callback: hàm được gọi khi task thất bại
   -  On_success_callback: hàm được gọi khi task thành công

### Operators
-   Mỗi operator đại diện cho 1 công việc cụ thể trong quy trình.
-   Các loại operator trong airflow được phân loại thành:
   -  Action Operators (Operator hành động): thực hiện các hành động cụ thể, như chạy lệnh, thực thi mã, hoặc gửi thông báo. Chúng thường được sử dụng để thực hiện các tác vụ xử lý hoặc thao tác cụ thể.
      -  BashOperator:  chạy các lệnh Bash hoặc script shell
      -  PythonOperator: thực thi các hàm python
      -  EmailOperator: Gửi mail thông qua STMP
      -  PythonVirtualenvOperator: thực thi các hàm python trong một môi trường ảo
   -  Transfer Operators (Operator truyền dữ liệu): sử dụng để di chuyển hoặc xử lý dữ liệu giữa các hệ thống hoặc dịch vụ.
      -  MysqlOperator: thực thi các lệnh SQL trên CSDL Mysql
      -  PostgresOperator: thực thi các lệnh SQL trên CSDL Postgres
      -  S3FileTransformOperator: Thực hiện các chức năng xử lý file trên Amazon S3
      -  SparkSqlOperator: Thực hiện các truy vấn Spark SQL
   -  Sensor Operators (Operator cảm biến): sẽ chờ đợi một điều kiện cụ thể được thỏa mãn trước khi tiếp tục thực thi.
      -  HdfsSensor: Kiểm tra sự tồn tại của 1 tệp trên HDFS
   -  Control Operators (Operator điều khiển): điều khiển luồng thực thi trong DAG
      -  DummyOperator: Được sử dụng để tạo các kết nối giữa các task


 
### Apache NiFi
-  Là một nền tảng tích hợp dữ liệu (data integration ) và xử lý luồng dữ liệu theo time thực hoặc theo lô(batch). Nifi được thiết kế để xử lý, chuyển đổi và định nghĩa tuyến dữ liệu từ nhiều nguồn đến nhiều đích khác nhau một cách dễ dàng và trực quan 
-  Điểm nổi bật của nifi là giao diện đồ họa(GUI) cho phép người dùng thiết kế luồng dữ liệu mà không cần viết mã phức tập
-  Các tính năng chính: 
   -  Giao diện đồ họa than thiện: cung cấp giao diện kéo – thả đơn giản
   -  Xử lý dữ liệu linh hoạt: có thể xử lý dữ liệu theo realtime hoặc theo batch
   -  Hỗ trợ đa dạng nguồn dữ liệu: Nifi có thể kết nối nhiều nguồn CSDL như SQL,NoSQL, hệ thống tệp, API,Kafka,Hadoop,…
   -  Quản lý luồng dữ liệu(Data Provenance): Nifi theo dõi toàn bộ hành chính của dữ liệu từ nguồn tới đích, giúp kiểm tra và phân tích nguồn gốc dữ liệu
   -  Khả năng mở rộng: có thể mở rộng theo cluster để xử lý dữ liệu lớn
   -  Xử lý lỗi: có cơ chế xử lý lỗi linh hoạt, cho phép tái thử(reply), định tuyến lại hoặc lưu trữ dữ liệu lỗi.
-  Các thành phần chinhs: 
   -  Flow file:Đơn vị dữ liệu cơ bản trong Nifi, chứa nội dung dữ liệu (content) và các thuộc tính liên quan
   -  Processor: Thành phần thực hiện các tác vụ như đọc, ghi, chuyển đổi, định tuyến dữ liệu.
   -  Connection: kết nối giữa các processor để truyền dữ liệu, hỗ trợ cơ chế xếp hàng(queue) và ưu tiên
   -  Process group: nhóm các processor để tổ chức và tái sử dụng luồng dữ liệu
   -  Controller services: dịch vụ dùng hcung như kết nối cở sở dữ liệu, cấu hình SSL
   -  Templates: cho phép lưu và tái sử dụng các luồng dữ liệu đã thiết keks
-  Cách hoạt động
   -  Nifi hoạt động dựa trên khái niện dataflow. Người dùng thiết kế luồng dữ liệu bằng cách kéo thả các processor và kết nối chúng trên giao diện web
   -  Dữ liệu lấy từ nguồn(source), xử lý qua các bước(chuyển đổi, lọc, làm giàu,…) sau đó gửi tới đich
  
### API integration
-  Là một phần mở rộng của API 
-  API integration là quá trình kết hợp nhiều API được cài trên phần mềm hoặc hệ thống để giao tiếp hoặc truyền dữ liệu
-  API integration giúp tự động hóa công việc, giảm thiểu công việc thủ công và tăng cường hiệu quả, tiết kiệm thời gian.
-  Các loại API Integration: Dựa vào giao thức và mục đích, API integration được chia vào các loại sau: 
   -  Public(Open) APIs: 
      -  Là các API công khai, được cung cấp cho mọi nhà phát triển hoặc người dùng bên ngoài mà không cần nhiều hạn chế.
   -  Partner-based APIs:
      - Là các API được cung cấp cho các đối tác cụ thể, thường yêu cầu thỏa thuận hợp tác hoặc xác thực (như API key, OAuth). Chúng có mức độ kiểm soát cao hơn so với Public APIs và thường được sử dụng trong các mối quan hệ kinh doanh
   -  Private (Internal) APIs
      - Là các API chỉ được sử dụng trong nội bộ tổ chức, không công khai ra bên ngoài. Chúng giúp các nhóm hoặc hệ thống trong cùng một công ty giao tiếp với nhau, tối ưu hóa quy trình phát triển và vận hành
   -  Composite APIs
      - Là các API kết hợp nhiều API hoặc điểm cuối (endpoints) để thực hiện nhiều tác vụ trong một lần gọi. Chúng giúp giảm số lượng yêu cầu mạng, cải thiện hiệu suất, thường được sử dụng trong các hệ thống phức tạp
-  Các Mô hình Tích hợp API Phổ biến
   -  Tích hợp B2B (Doanh nghiệp với Doanh nghiệp) Tích hợp API được sử dụng để kết nối giữa hai hoặc nhiều công ty/ tổ chức nhằm chia sẻ dữ liệu và tối ưu hóa quy trình kinh doanh. Ví dụ: Một công ty thương mại điện tử chia sẻ dữ liệu đơn hàng với đối tác vận chuyển.
   -  Chuyển giao dữ liệu theo lô (Batch Data Transfers) Chuyển giao dữ liệu theo lô liên quan đến việc xử lý các cơ sở dữ liệu lớn thành nhiều lô dữ liệu. Các lô này được tổng hợp hoặc thống nhất thành một định dạng dữ liệu duy nhất để có cái nhìn toàn diện và dễ hiểu hơn.
   -  Tự động hóa quy trình làm việc (Workflow Automation): Tích hợp API giúp tự động hóa các tác vụ và hoạt động của nhiều hệ thống hoặc ứng dụng, loại bỏ xử lý thủ công. Điều này giúp đơn giản hóa quy trình kinh doanh. Ví dụ: Gửi email tự động xác nhận sau khi đặt hàng là một trường hợp điển hình.
   -  Đồng bộ dữ liệu thời gian thực (Real-time Data Syncing): Khi các hệ thống hoặc phần mềm kết nối với nhau, việc đồng bộ hóa dữ liệu là cần thiết. Tích hợp API đảm bảo rằng mọi dữ liệu được truyền giữa các hệ thống được đồng bộ hóa chính xác và tức thời.
   -  Kết nối API tùy chỉnh (Custom API Connectors): Các kết nối API tùy chỉnh được thiết kế để đáp ứng nhu cầu tích hợp cụ thể của người dùng giữa các hệ thống hoặc ứng dụng. Mục đích là tạo ra các giải pháp tích hợp phù hợp với yêu cầu riêng biệt.
## Tuần 6: Production Pipeline
