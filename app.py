import streamlit as st 
from PIL import Image

image = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/profile2.jpeg")
image2 = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/model.jpg")
image3 = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/sanifly.jpg")
image4 = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/shibaura_institute_of_technology_tokyo_logo.png")
image5 = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/arimac.png")
image6 = Image.open("C:/Users/Dinuka's PC/Desktop/My Portfolio Website/images/usj.png")

st.set_page_config(page_title="My Webpage", page_icon=":smiley:", layout="wide")
 

with st.container():
    col1,col2 = st.columns((2,1))
    with col1:
        st.subheader("Hi, I am Dinuka :wave:")
        st.title("Dinuka Wijesundara")
        st.write("I'm a Fresh Graduate from University of Sri Jayewardenepura, Sri Lanka")
        st.write("""I completed my undergrad, BSc Business Information Systems (Special) degree at Departement of Information technology, University of Sri jayewardenepura, SriLanka.
        Where my bachelor's research and project were on Stock market price prediction using Deep Learning Neural networks, adviced by [Prof.Lasith Gunawardena.](https://mgt.sjp.ac.lk/itc/team_member/prof-k-s-lasith-gunawardena/)
        Previously I completed my research internship under the supervision of [Prof. Chinthaka Premachandra](https://shibaura.pure.elsevier.com/en/persons/chinthaka-premachandra) at [Departement of Electronic Engineering, Shibaura Institue of Technology, Koto ku, Japan.](https://www.shibaura-it.ac.jp/en/academics/engineering/ele.html)
        I gained industry experience working as an Artificial Intelligence Intern at Arimac, where my tasks were mainly focused on Deep learning with Computer Vision. 

        """)
        st.write(""" 
            I'm interested in broader areas in Deep Learning with Computer Vision and MLOps
        """)
        st.write("---")
with st.container():
  st.write("[Email](dilshanup125@gmail.com)   [Linkedin](https://Linkedin.com/in/dinuka-125)   [Github](https://github.com/dinuka125)  ")        

with st.container():
    st.subheader("News")   
    st.write("[Nov 2022]   Presented My Paper at [SCIS&ISIS 2022](http://soft-cr.org/scis/2022/index.html) -Ise-Shima, Mie, Japan 2022") 
    st.write("[Oct 2022]   Paper titled 'Human Recognition from High-altitude UAV Camera Images by AI based Body Region Detection' Accepted to the [SCIS&ISIS](http://soft-cr.org/scis/2022/index.html) 2022 Conference Japan ") 
    st.write("[Oct 2022]   Completed The AI Research internship at [SIT](https://www.shibaura-it.ac.jp/en/) Japan")     
    st.write("[Jun 2022]   Our team Ideacrushers emerged as Global Winners at [Commonwealth Digital Health Awards 2022](https://www.sjp.ac.lk/news/usj-team-won-eco-tech-category-at-the-5th-commonwealth-digital-health-awards-2022/) - IOT,ML,Cloud Computing")
    st.write("[Jan 2022]   Joined [Shibaura Institute of Technology](https://www.shibaura-it.ac.jp/en/) as AI Research Intern")  
    st.write("[Dec 2021]   Competed Artificial Intelligence inetership at Arimac") 
    st.write("[Nov 2021]   Our team Ideacrushers emerged as Second Runner Up at International ICT Innovative Services Awards 2021 - IOT,ML,Cloud Computing") 
    st.write("[Oct 2021]   Paper titled 'A Framework for Smartwash room accepted to [IEEE 10th Global Conference on Consumer Electronics 2021 -Japan](https://www.ieee-gcce.org/)")  
    st.write("[Jul 2021]   Joined Arimac as Artificial Intelligence Intern")
    st.write("[Mar 2021]   Our team Ideacrushers emerged as National Runner up and a Western Province Winner in Best Innovative Product/Project - University Category at SLASSCOM National Ingenuity Awards 2021, organized by SLASSCOM Sri lanka")  
   


    with col2:
        st.write("""
          <style>
            img {
            border: 5px solid #ddd;
            border-radius: 50%;
            width: 90%;
            height: 100%;
            padding: 5px;
            margin-left: auto;
          }
          img:hover {
            box-shadow: 0 0 2px 1px rgba(0, 140, 186, 0.5);
          }
          </style>
          """, unsafe_allow_html=True) 
        st.image(image) 


with st.container():
  st.subheader("Research")   
  st.write("""Talking about research interests in general, I’m interested in,Supervised learning, Reingforcement learning,  Deep learning with Computer Vision, Activity recognition, and object detection in edge devices.
  """)
  st.write("---")

with st.container():
  col1,col2 = st.columns((1,3))
  
  with col1:
    st.write("""
          <style>
            img {
            border: 5px solid #ddd;
            border-radius: 50%;
            width: 90%;
            height: 100%;
            padding: 5px;
            margin-left: auto;
          }
         
          </style>
          """, unsafe_allow_html=True) 
    st.image(image2)

  with col2:
    
    st.markdown("**1: Human Recognition from High-altitude UAV Camera Images by AI based Body Region Detection**")
    st.write("**Joint 12th International Conference on Soft Computing and Intelligent Systems and 23rd International Symposium on Advanced Intelligent Systems [(SCIS&ISIS 2022)](http://soft-cr.org/scis/2022/index.html) -Ise-Shima, Mie, Japan 2022**")
    st.write("**_Abstract_**")
    st.write(" The usage of unmanned aerial vehicles (UAVs) has rapidly increased during the recent past. The application areas for UAVs include search and rescue operations, tracking humans for surveillance, disaster management etc. In most such situations, the UAV's ability to automatically recognize humans, body regions, and other objects is crucial. Yet visibility issues may exist in UAV images resulting in challenges for object detection. In the case of recognizing humans from the high-altitude UAV camera images, conventional methods mostly recognize humans, based on the features of the entire body. Such methods are less effective when the parts of the body appear in the images, especially during highaltitude flights. In this paper, we develop a framework for human recognition by detecting the human body regions with YOLOv5 and Haar cascade classifier. The body part detection is done using YOLOv5, and then the output is forwarded to Haar cascade classifiers to classify body regions such as head, upper body, lower body. Human availability is confirmed, if the classified body part belongs to one of above body regions. We conducted experiments using the VisDrone data set. Preliminary results show promise on the effectiveness of the method.")
    st.write("---")

with st.container():
  col1,col2 = st.columns((1,3))
  
  with col1:
    st.image(image3)
  with col2:
    st.markdown("**2: A Framework for IoT-Enabled Smart Washrooms**")
    st.write("**2021 IEEE 10th Global Conference on Consumer Electronics (GCCE) - Kyoto, Japan**")
    st.write("**_Abstract_**  [Paper](https://ieeexplore.ieee.org/document/9622030)") 
    st.write(" Washrooms are a ubiquitous, yet essential element connected with day-to-day living environments. Public washrooms or restrooms are a common feature in all public buildings. They are often linked to the notion of “unclean” environments, due to the sheer number of people who use its services. From a health and safety perspective, it is imperative to maintain hygiene standards that will provide confidence to its users. This is especially true in the Covid-19 pandemic situation, where disinfection is of prime importance. Several elements contribute to a clean washroom, and some elements can benefit from Internet of Things (IoT) technologies. This paper introduces a framework for the use of IoT technology for implementing a Smart Washroom. Our research further explores public perception of clean washrooms and introduces a novel mobile app-based approach to locate clean public washrooms.")
    st.write("---")

      
with st.container():
  st.subheader("Experience") 

with st.container():  
  col1, col2 =st.columns((1,2))    

  with col1:
    st.image(image4) 

  with col2:
    st.markdown("**Shibaura Institue of Technology, Toyosu, Tokyo, Japan**")
    st.write("AI Research Intern  \nJan 2022 - Oct 2022")    
    
with st.container():  
  col1, col2 =st.columns((1,2))    

  with col1:
    st.image(image5) 

  with col2:
    st.markdown("**Arimac, Colombo, Sri Lanka**")
    st.write("AI Research Intern  \n Jul 2021 - Dec 2021")    

with st.container():
  st.subheader("Education") 

with st.container():  
  col1, col2 =st.columns((1,2))    

  with col1:
    st.image(image6) 

  with col2:
    st.markdown("**University of Sri Jayewardenepura, Sri Lanka**")
    st.write("Bachelor of Science in Business Information Systems (special)  \n Department of Information Technology  \n Oct 2017 - Oct 2022")        