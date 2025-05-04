# from src.agent import run_agent
#
#
# def main():
#     print("🔹 DeepSeek Agent (terminal mode). Type Ctrl-C or 'exit' to quit.\n")
#     try:
#         while True:
#             user_input = input("You: ").strip()
#             if user_input.lower() in ("exit", "quit"):
#                 print("Goodbye!")
#                 break
#             print(run_agent(user_input, 'default-session'))
#     except KeyboardInterrupt:
#         print("\nInterrupted. Goodbye!")
#
#
# if __name__ == "__main__":
#     main()

import gradio as gr
from src.agent import run_agent

# Optional: Patch for gradio_client schema issues (safe to include)
import gradio_client.utils as _gc_utils

_orig_get_type = _gc_utils.get_type
_orig_json_to_py = _gc_utils._json_schema_to_python_type


def _patched_get_type(schema):
    if isinstance(schema, bool):
        return "any"
    return _orig_get_type(schema)


def _patched_json_schema_to_python_type(schema, defs=None):
    if isinstance(schema, bool):
        return "any"
    return _orig_json_to_py(schema, defs)


_gc_utils.get_type = _patched_get_type
_gc_utils._json_schema_to_python_type = _patched_json_schema_to_python_type

# Gradio app
with gr.Blocks(title="DeepSeek Agent", fill_height=True) as demo:
    gr.Markdown("## 💬 DeepSeek Agent")

    chatbot = gr.Chatbot(
        label="Chat",
        placeholder="Ask something...",
        show_copy_button=True,
        render_markdown=True,
        layout="bubble",
        bubble_full_width=True,
        scale=9,
    )
    txt = gr.Textbox(
        placeholder="Type your message and hit Enter",
        show_label=False,
        lines=1,
        scale=1,
    )


    def chat_fn(user_message, chat_history):
        if chat_history is None:
            chat_history = []
        response = run_agent(user_message, thread_id="web-session")
        chat_history.append((user_message, response))
        return "", chat_history


    txt.submit(chat_fn, inputs=[txt, chatbot], outputs=[txt, chatbot])

if __name__ == "__main__":
    demo.launch(share=True)
