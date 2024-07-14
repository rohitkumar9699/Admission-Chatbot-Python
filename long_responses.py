import random
# Define the ans responses
Hostel_Fee = """
We believe in rendering a warm and pleasant environment where students can learn, live, relax and feel at home. From air-conditioned rooms,ko to 24/7 power supply and Wi-Fi facilities to multi-cuisine dining menus and full-time medical support, we take immense care in setting up a wholesome learning experience for our students.     \n
Hostel Fees 2023 - 24 (Domestic) - Hostel Fees (Hostel Facility For One Full Year Only)
----------------------------------------------------------------------------------------------------------------
No of Students Per Room   |   Type of Room    |   Room Rent (₹)   |   Mess Charges (₹)   |   Total Room Rent + Mess Charges (₹)   |   One time Refundable Caution Deposit (₹)   |   Total Payable (₹)
----------------------------------------------------------------------------------------------------------------
2 Sharing    |    AC    |    1,20,000    |    70,000    |    1,90,000    |    10,000    |    2,00,000
Non AC    |    80,000    |    70,000    |    1,50,000    |    10,000    |    1,60,000
3 sharing    |    AC    |    1,05,000    |    70,000    |    1,75,000    |    10,000    |    1,85,000
Non AC    |    70,000    |    70,000    |    1,40,000    |    10,000    |    1,50,000
4 sharing    |    AC    |    95,000    |    70,000    |    1,65,000    |    10,000    |    1,75,000
Non AC    |    60,000    |    70,000    |    1,30,000    |    10,000    |    1,40,000
4 sharing Bunker Bed    |    AC    |    60,000    |    70,000    |    1,30,000    |    10,000    |    1,40,000
Non AC    |    40,000    |    70,000    |    1,10,000    |    10,000    |    1,20,000
5 sharing    |    AC    |    85,000    |    70,000    |    1,55,000    |    10,000    |    1,65,000
Non AC    |    50,000    |    70,000    |    1,20,000    |    10,000    |    1,30,000
6 Sharing (Common Washroom)    |    AC    |    65,000    |    70,000    |    1,35,000    |    10,000    |    1,45,000
8 sharing    |    AC    |    60,000    |    70,000    |    1,30,000    |    10,000    |    1,40,000
Non AC    |    25,000    |    70,000    |    95,000    |    10,000    |    1,05,000
8 Sharing (Common Washroom)    |    AC    |    50,000    |    70,000    |    1,20,000    |    10,000    |    1,30,000
10 Sharing Bunker (6+4)    |    AC    |    50,000    |    70,000    |    1,20,000    |    10,000    |    1,30,000
Non AC    |    22,000    |    70,000    |    92,000    |    10,000    |    1,02,000
"""
fee_structure = """
Academic fee
Courses          Tution Fee          Duration 
------------------------------------------------
B.Tech           3.1 Lakhs pa         4 years 
BBA              1.6 lakhs pa         3 years 
B.Com            2 Lakhs pa           3 years 
BSc              1.9 Lakhs pa         3 Years 
BA               1.5 Lakhs pa         3 Years 
M.Tech           3 Lakhs pa           2 Years 
MSc              1.8 Lakhs pa         2 Years

To know the fee structure in detail 'https://srmap.edu.in/admission-india/hostel-fee-seas/'.
"""
Infrastructure = """
Designed by Perkins + Will →
----------------------------------------
This American architecture firm specializes in educational institutions and has been involved in developing some of the marquee structures in this category.

Learning happens everywhere →
----------------------------------------
At SRM AP, learning happens everywhere: In and out of the classroom, on and off campus, and in both formal and informal settings. Our buildings foster a new culture of learning that is multi-dimensional, global, social, experiential, and interactive.

A wide range of learning spaces →
----------------------------------------
From traditional classrooms to active, problem-based environments and adaptive learning, the latest technology for hybrid curricula, instant feedback, and immersive simulation environments.

Cutting-edge research facilities →
----------------------------------------
Research is a top priority at SRM University-AP. SRM AP has numerous international programs which emphasize cross-cultural exposure, learning and innovation, collaborating with world-leading academic and research institutions around the world. Here on our campus, digital learning takes a leading role in the transformation of teaching and learning and will, in return, lend itself to global accreditation.
"""
Library = """
SRM University-AP aims to build a world-class library for the benefit of students, faculty, and researchers. Our aim is to build one of the best international libraries according to International Standards. Now, the University library has an excellent collection of books covering various branches of Engineering and Sciences, Entrepreneurship & Management, Liberal Arts & Social Sciences, and their related fields.

For more details, 'https://srmap.edu.in/library/'.
"""
Transport_Fee = """
TRANSPORT FEES 2023 - 24 (Applicable for day scholars only) (*Transportation Facility For One Full Year Only)
------------------------------------------------------------------------------------------------------------
Distance Range (Both Ways)    |    Fee
------------------------------------------------------------------------------------------------------------
01 - 30 Kms                   |    ₹ 60,000/-
31 - 60 Kms                   |    ₹ 65,000/-
61 Kms and Above              |    ₹ 70,000/-

Transportation will be provided based on the availability of seats.
"""
Bus_Route = """
The university offers bus transportation facilities covering various routes to facilitate commuting for students, faculty, and staff. For detailed information on bus routes and boarding points, please refer to the 'https://srmap.edu.in/wp-content/uploads/2023/04/srmaproute-wise-boarding-point-report-v1.pdf?x91100'.
"""

Faculty = """
The faculty members at SRM University-AP are highly experienced and renowned in their fields. To explore our faculty members and their expertise, visit: 'https://srmap.edu.in/faculty-4/'.
"""
Placements = """
The placement rate recorded during SRM AP BTech CSE, BTech ECE, and BSc Computer Science placements 2023 was 100%. Further, the highest package and average package offered during SRM University AP BTech CSE placements 2023 stood at INR 50 LPA and INR 9.90 LPA, respectively.
For information about placements and career development opportunities, visit the 'https://srmap.edu.in/crcs/'.
"""
Medical_facilities = """
Medical services:
- Outpatient Department (OPD) services
- Emergency services
- Emergency referral services
- Oxygen & nebulization
- Rabies vaccine, Anti-snake venom
- Provision of all first aid medicines, injections, emergency drugs, IV Fluids, etc.
- Suturing of wounds
- First aid training provided to wardens, NSS students, security personnel, and other interested staff and faculty
- Health education and awareness sessions

Our medical facilities are equipped to provide comprehensive healthcare services to our students, faculty, and staff, ensuring their well-being and safety on campus.
"""

B_Tech_courses ="Civil Engineering, Computer Science, Electrical and Electronics, Electronics and Communication, and Mechanical Engineering."
scholarships_Type = "SRM University-AP offers various scholarships to meritorious students based on academic accomplishments, sports and cultural excellence, as well as to economically challenged and differently abled students.\nSRM Merit Scholarship under School of Engineering.\nSRMJEEE rank 101 to 500: 100% Tuition fee waiver.\nSRMJEEE rank 501 to 1000: 75% Tuition fee waiver.\nSRMJEEE rank 1001 to 2000: 50% Tuition fee waiver.\nSRMJEEE rank 2001 to 3000: 25% Tuition fee waiver"
College_Info = "SRM University Amaravati is a Deemed University that was established in the year 2017. \nThe University is a part of the SRM Group and is situated in Guntur, Andhra Pradesh. The university has collaborated with the University of California Berkeley, MIT USA and EFREI France. \nSRM University Amaravati is a multi-stream research university that offers degree and research programs in diverse fields like Civil Engineering, Computer Science, Electrical and Electronics, Electronics and Communication, and Mechanical Engineering."
get_admission =""" For admission to undergraduate programs, please fill out the admission form available at: 'https://applications.srmap.edu.in/ug-application-form?utm_source=google&utm_medium=organic&utm_campaign=vb-admission-2024'."""

many_campuses = "SRM Institute of Science and Technology includes six campuses, four in Tamil Nadu — Kattankulathur, Ramapuram and Vadapalani, and Tiruchirappalli, one in Amaravati,Andhra Pradesh and one in NCR Delhi."""

ratio = "SRM AP has a student-faculty ratio of 14:1"
collaborations = "SRM University AP has international collaborations with many universities around the world such as University of Berkeley, University of Wisconsin-Madison, a few (be it in SAP collaboration or for a dual degree\). SRM University-AP is recognized across the country for its high standards of education, exciting opportunities and excellent placement."
student_clubs = "There are several student clubs and organizations you can join sach as Esports.\nPhotography Club.\nRealistic Dance Club.\nMusic Club.\nACTS.\nCreative Arts Club.\nAnime Society."
sports_facilities = "The sports club is a zealous group of talented sportspersons who promote team spirit, leadership, and fitness. The club hosts numerous competitions around the year for students of SRM University-AP, Andhra Pradesh across all schools and streams."
change_branch = "If you want to change your branch, you need to follow the process which will be told to you by admission department"
courses_available = """
SRM AP offers a range of undergraduate, postgraduate, and doctoral courses under various schools such as School of Engineering and Applied Sciences (for BTech & MTech), School of Liberal Arts and Basic Sciences (for BA, BSc & BCom), and School of Management (for BBA Hons and MBA Banking and Financial Services). The university also offers scholarships to meritorious students. For more details and admission procedures, visit: 'https://srmap.edu.in/indian-admission/.
"""
top_companies = "Top recruiting companies are Amazon, ABInBev, PayPal, Western Digital, Optum, TCS, Cognizant, Capgemini, Quinbay, AppViewX and many more companies"
extracurricular_activities = "Apart from the curriculum, there are various extracurricular activities clubs and sports"

def unknown():
    response = [
        'Could you please rephrase that?',
        'I didn\'t quite get that, could you repeat?',
        'I\'m not sure I understand, could you provide more context?'
    ]
    return random.choice(response)
