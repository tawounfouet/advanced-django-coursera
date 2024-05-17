# Question 3

The view question3 has been set up with the URL /question3/. It renders the template question3.html. There is a <div id="question3"> in this template that contains the current time. Cache the contents of this div, but not the rest of the template or the response. You do not need to cache differently for different users.

## Testing Your Code
- The <h1> text changes on each reload.
- The <h2> text only changes after waiting two minutes.


## Problem

```html
{# Question 3: Load any libraries you need here #}
{# Question 3: Don't cache this first <h1> element #}
<h1>The Uncached Time Is {% now "c" %}</h1>
<div id="question3">
    {# Question 3: Cache the contents of this div (not including the <div> or </div> tags) #}
    <h2>The Cached Time Was {% now "c" %}</h2>
</div>
```

## Solution

```html
{# Question 3: Load any libraries you need here #}
{# Question 3: Don't cache this first <h1> element #}
<h1>The Uncached Time Is {% now "c" %}</h1>
<div id="question3">
    {# Question 3: Cache the contents of this div (not including the <div> or </div> tags) #}
    {% load cache %}
    {% cache 120 question3_cache %}
        <h2>The Cached Time Was {% now "c" %}</h2>
    {% endcache %}
</div>
```

- Load the cache template tag
- Start a cache tag inside the div with the ID "question3"
- In the cache tag, use 120 to cache for two minutes and current_time as the value to be cached
- End with an endcache tag