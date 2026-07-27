# Imagery

The catalog bans stock photos, 3D blobs, faceless people holding orbs and re-drawn
browser chrome. That leaves a hole, and a hole is why generated pages end up as walls of
text in boxes. This file is what goes in the hole.

## You must land on one of these

Work down the list and commit to the first the brief can support. **This list has no
"skip" option.** An earlier version ended with "nothing" as a legitimate answer and
models took it every time: across six matched pairs, guided pages shipped 1 SVG between
them against 114 in the unguided baselines. Absence is not restraint, it is an unmade
decision.

1. **The real thing.** The actual product surface, the actual data, the actual document.
   Measured on 8 handmade sites: Linear argues by showing app UI, Panic by showing the
   games it publishes, Pentagram by showing 81 pieces of work. None of them illustrate a
   concept. If you have a thing, show the thing.
2. **The real thing, drawn.** When you cannot ship a screenshot, build the object in the
   page itself with CSS and SVG. A bake schedule, a year of habit squares, a ledger, a
   signal chain. These are cheap, they never 404, they scale, and they cannot be mistaken
   for someone else's stock library.
3. **A diagram that carries information.** Not an "illustration of collaboration". A
   real explanatory drawing: how the lanes share slots, how the money moves, what
   recomputes when you write to a source. If someone could learn something from it, it
   earns its space.
4. **Texture and material.** Paper grain, a halftone, a print misregistration, a
   photographic scan. Carries mood without pretending to carry meaning.
5. **Type as the image.** Set something enormous and let the page be typographic.
   Legitimate, and often the strongest answer for editorial work.
6. **Deliberate emptiness, and only for genuine tool surfaces.** A settings panel or an
   internal dashboard can legitimately carry no imagery, because the data is the image.
   A shop, a person, a product, an event or anything with a mood cannot. If you reach
   this rung on a brief with warmth in it, you went too far down the list: go back to
   rung 2 and draw the thing.

## Photography, if you use it

- One source, one treatment. Mixed crops, mixed grain and mixed colour temperature is
  the single fastest way to look assembled from a search results page.
- Commit to a crop. The default centred 16:9 is the visual equivalent of Inter 700.
- Duotone, high-contrast black and white, or a consistent grade beats "natural" if the
  photos come from more than one shoot.
- Never the generic set: diverse team at a laptop, handshake, glass office, aerial
  desk-with-coffee.

## SVG, the default medium

Most of what a generated page needs is better as inline SVG than as an image file.

- It inherits `currentColor`, so it themes for free.
- It stays sharp, has no network cost, and cannot break a layout with a slow load.
- It can be *made of the data*, which is the difference between a chart and a picture of
  a chart.

Draw with intent: consistent stroke width across a set, aligned to a pixel grid at the
size it actually renders, geometry that survives at 16px.

## Icons

One set, at text size, optically aligned to the baseline. Or none.

- No emoji. Ever, as icons.
- No single giant centred icon above a heading, which is the shape of a slide.
- Do not mix outline and filled sets, and do not mix two libraries.
- An icon beside a label is usually redundant; the label is already doing the work. Icons
  earn their place in dense tools where they replace text, not in marketing pages where
  they decorate it.

## Alt text and figures

Alt text carries the meaning, not the filename and not the word "image". A decorative
graphic takes `alt=""` so a screen reader skips it rather than reading noise. If a
diagram teaches something, its meaning belongs in text nearby too, because that is the
only version that survives being read aloud, printed, or pasted into a chat.

## Two tests, and you need both

**The subtraction test.** Cover every image. If the page communicates exactly as much
without them, they were decoration. Make them carry information or remove them.

**The addition test, which is the one that was missing.** Describe your finished page to
someone in one sentence without using the words layout, spacing, typography or clean. If
the only honest description is "text and lines", the page has no visual argument. A
reader should be able to remember one image, object or moment a day later. Name it before
you ship. If you cannot, go back to rung 2 and draw something.

Both tests have to pass. The first stops decoration. The second stops emptiness, and
emptiness is the failure this skill was previously causing.
