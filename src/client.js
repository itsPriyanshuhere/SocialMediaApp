import {createClient} from '@sanity/client';
import imageUrlBuilder from '@sanity/image-url';

export const client = createClient({
    projectId: 'u53ul0xo',
    dataset: 'production',
    apiVersion: '2021-03-25',
    useCdn: true,
    token: 'skFZUs0WldyHyutvPO4dndf5vQci8TZ7DKBcKQEoDiwa89KJImJG4sGQBGs9QvPPYGIt2gW2zChQ1sfA9wCWsIOUwekbPxH2SiQeqnvuEbOC8rj5K6rxs9BXj2Reg1u8f34bpWAiEZiRc6b4ZIacybuFfkUIYzaOFAn6mO31Mk0xEsbmXn5C',  
});

const builder = imageUrlBuilder(client);

export const urlFor = (source) => builder.image(source);