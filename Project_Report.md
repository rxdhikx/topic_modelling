# Instagram Post Topic Modeling and Dimensional Quantification

### **Project Overview**
This project involves analyzing an Excel file containing Instagram post data to perform **topic modeling** and **dimensional quantification**. The data consists of various sheets, each representing a post, with the caption and associated comments. The goal is to identify key **themes or topics** that emerge from the posts and comments, and quantify **dimensions** (such as sentiment or engagement metrics).

### **Technologies Used**
- **Python**: The primary programming language used to implement the solution.
- **Transformers Library**: Provides access to large pre-trained language models (LLMs) like Flan-T5 for text generation and topic modeling.
- **PyTorch**: Framework used for running deep learning models, including Flan-T5, on GPUs for faster processing.
- **Pandas**: Data manipulation library used to load and process the Excel sheets and comments data.
- **Google Colab**: Cloud-based environment providing GPU support for efficient model inference.
- **OpenPyXL**: Library used for reading and processing Excel files.

### **Why Use LLMs for Topic Modeling?**
**Large Language Models (LLMs)** such as **Flan-T5** are capable of understanding natural language and generating meaningful output based on input data. In the context of this project:
- **Flan-T5** was chosen for **topic modeling** because it can generate coherent and relevant summaries based on large volumes of text, like Instagram captions and comments.
- The model processes unstructured text data, helping identify **latent topics** and **themes** from comments that are often varied and informal.
- LLMs allow us to quickly generate **insights from large datasets** without the need for manually tagging or classifying the data, making the process more efficient.

### **Situation**
The project started with an Excel file, **"Miquela Instagram Post_clean data.xlsx"**, containing multiple sheets (e.g., **Netflix**, **Burberry**, **Ory**) that represented Instagram posts and their associated comments. The goal was to perform an analysis to uncover the most relevant topics or themes from the captions and comments for each post.

Each sheet consisted of:
1. A **caption** (text description of the post).
2. A list of **comments** (user responses to the post).

As a data analyst, the task was to:
1. **Load** and process the data from multiple sheets.
2. **Identify themes** from the post and comments using topic modeling.
3. **Quantify dimensions**, such as engagement or sentiment metrics.

### **Task**
The main tasks for this project were:
1. **Topic Modeling**: Identify key themes and topics from the post captions and their associated comments.
2. **Quantify Dimensions**: Measure certain metrics from the comments, such as sentiment or engagement.
3. **Efficient Processing**: Process large datasets efficiently by using a batch processing approach and leveraging cloud GPU resources (Google Colab).
4. **Generate Reports**: Create easy-to-understand outputs (e.g., CSV files) with topics and metrics, suitable for further analysis or reporting.

### **Action**
To accomplish the task, the following actions were taken:

1. **Loading and Preprocessing Data**:
   - Used the **Pandas** library to load the Excel sheet data into Python.
   - Combined the post captions and comments to create a textual prompt for the topic modeling task.

2. **Topic Modeling with Flan-T5**:
   - **Flan-T5** (a large pre-trained model from Google) was used to generate relevant topics based on the combined captions and comments.
   - We created a **pipeline** for text generation using the model, passing the concatenated captions and comments as input.
   - The model was fine-tuned for topic generation tasks by providing a prompt like:
     ```
     "Post Caption: <caption_text> Comments: <comments_text>"
     ```
   - This prompt structure helped the model identify underlying topics from the text data.

3. **Batch Processing for Efficiency**:
   - Given the large number of sheets in the Excel file, the data was split into smaller **batches** of sheets to ensure efficient processing without overloading the system.
   - Each batch was processed sequentially, and the results were saved after each batch, reducing the likelihood of memory issues.

4. **Dimensional Quantification**:
   - Although the main task was topic modeling, additional **metrics like sentiment** and **engagement** were also computed from the comments, using predefined metrics or sentiment analysis models.

5. **Output and Report Generation**:
   - After processing, the results (i.e., topics and their relevance) were saved to **CSV files**, allowing for easy access and further analysis.
   - Intermediate results were saved for each batch to ensure progress tracking.

### **Results**
The project achieved the following outcomes:
1. **Topic Modeling Results**:
   - Generated meaningful themes and topics for each post, which can be used to better understand the discussions around the posts.
   - The model identified key trends and topics such as “fashion,” “product quality,” and “customer service” from the comments related to brands like Burberry and Netflix.

2. **Efficient Data Processing**:
   - By processing the sheets in batches, we ensured that the system handled the data efficiently and avoided memory overloads, despite the large volume of comments.

3. **Quantified Metrics**:
   - Although the primary focus was topic modeling, basic engagement and sentiment metrics were also extracted to provide a more complete analysis of the data.

4. **Reports**:
   - Generated CSV files with the extracted topics and their relevance for each post.
   - Provided clear, actionable insights based on the analysis of Instagram captions and comments.

### **Conclusion**
This project demonstrated the power of **Large Language Models (LLMs)** like **Flan-T5** in performing complex natural language processing tasks such as **topic modeling** and **dimensional quantification** on large-scale text data. The combination of **batch processing** and leveraging cloud-based **GPU resources** allowed for efficient analysis of large datasets, yielding valuable insights from Instagram posts and their associated comments.

By using **Flan-T5**, we were able to quickly generate **meaningful topics** from user comments and quantify the **engagement** of Instagram posts. This analysis can be extended to other types of social media data, providing insights into user sentiment, behavior, and interactions with posts.

### **Future Work**
- **Refinement of Topic Models**: Explore advanced techniques to improve the granularity and accuracy of the topics identified.
- **Advanced Quantification**: Implement more advanced metrics for sentiment analysis and engagement quantification.
- **Visualization**: Create visualizations (e.g., word clouds, topic heatmaps) for better insights from the analysis.

### **Technologies Used**:
- **Python**
- **Transformers Library**
- **PyTorch**
- **Pandas**
- **Google Colab**
- **OpenPyXL**
