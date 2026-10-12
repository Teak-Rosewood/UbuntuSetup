# AI command completion for bash using the GitHub Copilot CLI.
#
# Type a description (or half a command) and press Ctrl+G. The line is replaced
# by a suggested command. It is never run automatically: review, edit, Enter.
#
#   AI_MODEL   model to use (default gpt-5-mini, a cheap one)

: "${AI_MODEL:=gpt-5-mini}"

_ai_complete() {
    local input="$READLINE_LINE" out
    [ -z "${input//[[:space:]]/}" ] && return
    command -v copilot >/dev/null || { READLINE_LINE="# copilot CLI not installed"; READLINE_POINT=${#READLINE_LINE}; return; }

    printf '\r\033[K\033[2m  thinking...\033[0m'
    out=$(copilot -s --no-custom-instructions --model "$AI_MODEL" -p \
"You are a bash command generator on Ubuntu Linux. Current directory: $PWD.
Turn the following request (or partial command) into ONE bash command line.
Output only the command: no explanation, no markdown, no code fences.
If it is destructive, still output it; the user reviews before running.
Request: $input" 2>/dev/null)
    printf '\r\033[K'

    # Strip code fences and keep the first non-empty line
    out=$(printf '%s\n' "$out" | sed -e '/^```/d' -e '/^[[:space:]]*$/d' | head -n1)
    [ -z "$out" ] && return
    READLINE_LINE="$out"
    READLINE_POINT=${#READLINE_LINE}
}

[[ $- == *i* ]] && bind -x '"\C-g": _ai_complete'
