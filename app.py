import streamlit as st
import os
from groq import Groq
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(
    page_title="GameCode Enhancer - AI Code Iterator for Game Developers",
    layout="wide"
)

# Fetch the Groq API key from environment
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    st.sidebar.error("Missing GROQ_API_KEY in .env file. Please add it and restart.")

# Initialize Groq client (will use environment variable)
client = Groq()

# Function to process code with Llama 3 via Groq
def process_code_with_ai(code, instruction, language):
    try:
        # Create a prompt for the LLM that gives context about game development
        prompt = f"""You are a specialized AI assistant for game developers working with {language}.

Your task is to improve the following code according to the developer's instruction.
Focus on game development best practices, performance optimization, and clean code design.

ORIGINAL CODE:
```{language}
{code}
```

DEVELOPER'S INSTRUCTION:
{instruction}

Respond with:
1. Improved code between <IMPROVED_CODE> tags
2. Then provide a clear explanation of all changes made and why they improve the code
3. Focus specifically on game development considerations"""

        # Call the Groq API with Llama 3
        response = client.chat.completions.create(
            model="llama3-70b-8192",  # Using Llama 3 70B model
            messages=[{"role": "user", "content": prompt}],
            temperature=0.3,
            max_tokens=4000,
        )

        ai_response = response.choices[0].message.content

        # Extract the improved code
        if "<IMPROVED_CODE>" in ai_response and "</IMPROVED_CODE>" in ai_response:
            improved_code = ai_response.split("<IMPROVED_CODE>")[1].split("</IMPROVED_CODE>")[0].strip()
            explanation = ai_response.split("</IMPROVED_CODE>")[1].strip()
        else:
            # Fallback if tags aren't used correctly
            improved_code = "/* AI couldn't properly format the response. Please try again. */"
            explanation = ai_response

        return improved_code, explanation

    except Exception as e:
        return None, f"Error processing code: {str(e)}"


# UI for the Streamlit app
def main():
    st.title("GameCode Enhancer")
    st.subheader("AI-powered code improvement tool for game developers")

    # Sidebar for setup
    with st.sidebar:
        st.header("Setup")
        st.markdown(".env GROQ_API_KEY will be used automatically.")

        st.markdown("---")
        st.header("Language")
        language = st.selectbox(
            "Select game development language",
            ["Unity C#", "Godot GDScript", "Unreal C++", "JavaScript (HTML5 games)", "Python (PyGame)"]
        )

        st.markdown("---")
        st.markdown("### About")
        st.markdown(
            "GameCode Enhancer helps game developers improve their code with AI suggestions tailored for game development.")

    # Main content area - split into columns
    col1, col2 = st.columns([1, 1])

    with col1:
        st.header("Original Code")
        code_input = st.text_area(
            "Paste your game code here",
            height=400,
            placeholder="// Paste your game code here...",
            key="original_code"
        )

        st.subheader("What would you like to improve?")
        instruction = st.text_area(
            "Describe what you want improved (performance, readability, bug fixes, etc.)",
            placeholder="Example: Optimize this character movement code for better performance",
            key="instruction"
        )

        process_button = st.button("Enhance My Code", type="primary")

    # Process when button is clicked
    if process_button and code_input and instruction:
        if not api_key:
            st.error("Please set GROQ_API_KEY in your .env file before proceeding.")
        else:
            with st.spinner("AI is analyzing your code..."):
                improved_code, explanation = process_code_with_ai(code_input, instruction, language)

                if improved_code is None:
                    st.error(explanation)
                else:
                    # Store results in session state to preserve between reruns
                    st.session_state.improved_code = improved_code
                    st.session_state.explanation = explanation
                    st.session_state.show_results = True

    # Display results in second column
    with col2:
        st.header("Enhanced Code")

        if 'show_results' in st.session_state and st.session_state.show_results:
            st.code(st.session_state.improved_code, language=language.split()[0].lower())

            # Add button to apply changes
            if st.button("📋 Copy Enhanced Code"):
                st.success("Enhanced code copied to clipboard!")

            # Button to apply directly to original
            if st.button("🔄 Replace Original Code"):
                st.session_state.original_code = st.session_state.improved_code
                st.rerun()

            st.header("Explanation of Changes")
            st.markdown(st.session_state.explanation)
        else:
            st.info("Enhanced code will appear here after processing.")

    # Example section
    st.markdown("---")
    with st.expander("Show Example Game Code"):
        st.markdown("### Unity C# Character Controller Example")
        example_code = """using UnityEngine;

public class PlayerController : MonoBehaviour
{
    public float moveSpeed = 5f;

    void Update()
    {
        float horizontalInput = Input.GetAxis("Horizontal");
        float verticalInput = Input.GetAxis("Vertical");

        Vector3 movement = new Vector3(horizontalInput, 0f, verticalInput);
        transform.Translate(movement * moveSpeed * Time.deltaTime);

        if(movement != Vector3.zero)
        {
            transform.rotation = Quaternion.LookRotation(movement);
        }
    }

    void OnCollisionEnter(Collision collision)
    {
        if(collision.gameObject.tag == "Enemy")
        {
            Debug.Log("Player hit enemy");
        }
    }
}"""
        st.code(example_code, language="csharp")
        st.markdown(
            "Example improvement prompt: 'Optimize this character controller for better performance and add jump functionality'")


if __name__ == "__main__":
    main()