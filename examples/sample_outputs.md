# Sample Outputs

## Example 1: Reddit URL

Input:

```text
https://www.reddit.com/r/example/comments/abc123/example_thread/
```

Suggested assistant response:

```text
Reddit is high-risk for Claude-style retrieval. Direct fetches are often blocked, partial, or unreliable. Paste the post/comments you want analyzed, or upload screenshots/exported text.
```

## Example 2: X / Twitter URL

Input:

```text
https://x.com/user/status/123456789
```

Suggested assistant response:

```text
X/Twitter is high-risk for direct fetching because public pages are often restricted, login-gated, or incomplete for non-whitelisted bots. Paste the post/thread text or upload a screenshot.
```

## Example 3: Paywalled news article

Input:

```text
https://www.ft.com/content/example
```

Suggested assistant response:

```text
This source is likely paywalled or restricted. I should not repeatedly attempt to fetch it. Paste the article text you have access to, and I can summarize or analyze it.
```

## Example 4: Public GitHub repo

Input:

```text
https://github.com/example/project
```

Suggested assistant behavior:

```text
Public GitHub repos are usually reasonable to fetch directly. Proceed with normal retrieval unless the specific file is too large, private, or rate-limited.
```

## Example 5: Unknown domain

Input:

```text
https://random-saas-blog.example/post
```

Suggested assistant behavior:

```text
Try once. If retrieval fails or returns incomplete content, stop and ask the user to paste or upload the source material.
```
