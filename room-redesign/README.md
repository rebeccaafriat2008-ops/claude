# Bedroom redesign plan

Frozen briefs and exact prompts for three `/banana` photo edits, one per view:

| View | Brief | Prompt |
|---|---|---|
| Bed wall | `bed.brief.json` | `bed.prompt.txt` |
| Desk and window | `desk.brief.json` | `desk.prompt.txt` |
| Closet and door | `closet.brief.json` | `closet.prompt.txt` |

Settings for each: model `gemini-3.1-flash-image`, 1K, 9:16, JPEG, no storage,
no Search. Nominal cost about $0.067 per image (not a cap).

Reference alias, role, and purpose per view (must match the brief):

- bed: `--reference-name "bed wall photo"`
- desk: `--reference-name "desk and window photo"`
- closet: `--reference-name "closet and door photo"`
- all: `--reference-role object --reference-purpose "preserve room geometry, furniture and camera view" --reference-subject-id bedroom --model gemini-3.1-flash-image --aspect-ratio 9:16 --resolution 1K --label room-<view>`

The room photos themselves are not stored here; attach them in the session.
