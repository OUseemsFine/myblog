function convertBlog(blog){
    let cvt_abstract = blog.abstract;
    let cvt_content = blog.content;
    const cvt_blog = {
        abstract: cvt_abstract,
        content: cvt_content,
    }
}

function get_genre(genre){
    const genre_mapping = {
        'd':'Diary',
        'r':'Review',
        's':'Summary',
    }
    return genre_mapping[genre];
}