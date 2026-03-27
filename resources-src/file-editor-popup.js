import {EditorState} from "@codemirror/state"
import {EditorView} from "@codemirror/view"
import {basicSetup} from "codemirror"
import {python} from "@codemirror/lang-python"
import {json} from "@codemirror/lang-json"
import {javascript} from "@codemirror/lang-javascript"
import {markdown} from "@codemirror/lang-markdown"
import {html} from "@codemirror/lang-html"
import {css} from "@codemirror/lang-css"
import {xml} from "@codemirror/lang-xml"
import {yaml} from "@codemirror/lang-yaml"
import {sql} from "@codemirror/lang-sql"
import {java} from "@codemirror/lang-java"
import {php} from "@codemirror/lang-php"
import {rust} from "@codemirror/lang-rust"
import {cpp} from "@codemirror/lang-cpp"

function languageForPath(path) {
  const lower = String(path || "").toLowerCase()
  if (lower.endsWith(".py")) return python()
  if (lower.endsWith(".json")) return json()
  if (lower.endsWith(".js") || lower.endsWith(".mjs") || lower.endsWith(".cjs") || lower.endsWith(".jsx")) return javascript()
  if (lower.endsWith(".ts")) return javascript({typescript: true})
  if (lower.endsWith(".tsx")) return javascript({typescript: true, jsx: true})
  if (lower.endsWith(".md")) return markdown()
  if (lower.endsWith(".html")) return html()
  if (lower.endsWith(".css")) return css()
  if (lower.endsWith(".xml") || lower.endsWith(".svg")) return xml()
  if (lower.endsWith(".yml") || lower.endsWith(".yaml")) return yaml()
  if (lower.endsWith(".sql")) return sql()
  if (lower.endsWith(".java")) return java()
  if (lower.endsWith(".php")) return php()
  if (lower.endsWith(".rs")) return rust()
  if (/\.(c|cc|cpp|h|hpp)$/.test(lower)) return cpp()
  return []
}

function editorTheme() {
  return EditorView.theme({
    "&": {
      height: "100%",
      color: "#2d2216",
      backgroundColor: "transparent",
    },
    ".cm-content": {
      caretColor: "#8d4519",
    },
    ".cm-cursor, .cm-dropCursor": {
      borderLeftColor: "#8d4519",
    },
    ".cm-selectionBackground, .cm-content ::selection": {
      backgroundColor: "rgba(173, 92, 43, 0.18)",
    },
    ".cm-activeLine": {
      backgroundColor: "rgba(173, 92, 43, 0.06)",
    },
    ".cm-activeLineGutter": {
      backgroundColor: "rgba(173, 92, 43, 0.08)",
    },
  })
}

export function createFileEditor({parent, doc, filePath, onChange}) {
  return new EditorView({
    state: EditorState.create({
      doc,
      extensions: [
        basicSetup,
        EditorView.lineWrapping,
        editorTheme(),
        languageForPath(filePath),
        EditorView.updateListener.of(update => {
          if (update.docChanged && onChange) onChange(update.state.doc.toString())
        }),
      ],
    }),
    parent,
  })
}