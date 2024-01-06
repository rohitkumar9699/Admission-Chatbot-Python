
import random
# Define the ans responses
ADVICE = "Here is some advice..."
EATING = "I eat virtual food."
scholarships_Type = "SRM scholarships are awarded based on academic accomplishments, sports and cultural excellence. Means scholarships are also available for economically challenged and differently abled students.\nSRM Merit Scholarship under School of Engineering.\nSRMJEEE rank 101 to 500: 100% Tuition fee waiver.\nSRMJEEE rank 501 to 1000: 75% Tuition fee waiver.\nSRMJEEE rank 1001 to 2000: 50% Tuition fee waiver.\nSRMJEEE rank 2001 to 3000: 25% Tuition fee waiver"
College_Info = "Established in 2017, SRM University, (also known as SRM Amravati), Andhra Pradesh, is a private university that is a part of the SRM Group of Institutions. This is the first University in India to have an academic partnership with Minerva. SRM AP offers a range of undergraduate, postgraduate, and doctoral courses under various schools such as School of Engineering and Applied Sciences (for BTech & MTech), School of Liberal Arts and Basic Sciences (for BA, BSc & BCom), and School of Management (for BBA Hons and MBA Banking and Financial Services). The university also offers scholarships to meritorious students."
get_admission = "To get admission, you need to follow the admission process..."
many_campuses = "SRM Institute of Science and Technology includes six campuses, four in Tamil Nadu — Kattankulathur, Ramapuram and Vadapalani, and Tiruchirappalli, one in Amaravati,Andhra Pradesh and one in NCR Delhi."
hostel = "At SRM University-AP, we nurture a close-knit and lively residential space with state-of-the-art infrastructure catering to the needs of students. We believe in rendering a warm and pleasant environment where students can learn, live, relax and feel at home. From air-conditioned rooms to 24/7 power supply and Wi-Fi facilities to multi-cuisine dining menus and full-time medical support, we take immense care in setting up a wholesome learning experience for our students.     "
ratio = "SRM AP has a student-faculty ratio of 14:1"
collaborations = "SRM University AP has international collaborations with many universities around the world such as University of Berkeley, University of Wisconsin-Madison, a few (be it in SAP collaboration or for a dual degree\). SRM University-AP is recognized across the country for its high standards of education, exciting opportunities and excellent placement."
student_clubs = "There are several student clubs and organizations you can join sach as Esports.\nPhotography Club.\nRealistic Dance Club.\nMusic Club.\nACTS.\nCreative Arts Club.\nAnime Society."
sports_facilities = "The sports club is a zealous group of talented sportspersons who promote team spirit, leadership, and fitness. The club hosts numerous competitions around the year for students of SRM University-AP, Andhra Pradesh across all schools and streams."
change_branch = "If you want to change your branch, you need to follow the process which will be told to you by admission department"
courses_available = "SRM AP offers a range of undergraduate, postgraduate, and doctoral courses under various schools such as School of Engineering and Applied Sciences (for BTech & MTech), School of Liberal Arts and Basic Sciences (for BA, BSc & BCom), and School of Management (for BBA Hons and MBA Banking and Financial Services). The university also offers scholarships to meritorious students. ."
placements = "The placement rate recorded during SRM AP BTech CSE, BTech ECE, and BSc Computer Science placements 2023 was 100%. Further, the highest package and average package offered during SRM University AP BTech CSE placements 2023 stood at INR 50 LPA and INR 9.90 LPA, respectively. A total of 105 super dream offers and 11 International offers were received during placements 2023. Earlier, the highest package and average package offered during SRM University Andhra Pradesh MBA placements 2022 stood at INR 31 LPA and INR 7.75 LPA, respectively. The top recruiters during SRM AP placements 2023 included leading companies such as Amazon, TCS, IBM, Microsoft, TATA, etc.  "
top_companies = "Top recruiting companies are Amazon, ABInBev, PayPal, Western Digital, Optum, TCS, Cognizant, Capgemini, Quinbay, AppViewX and many more companies"
Faculty = "The faculty members have vast experience and expertise..."
extracurricular_activities = "Apart from the curriculum, there are various extracurricular activities clubs and sports"
fee_structure = "The fee structure varies based on the course and category..."
def unknown():
    response = ['Could you please re-phrase that?',
                '...',
                'What does that mean?'][random.randrange(3)]
    return response
