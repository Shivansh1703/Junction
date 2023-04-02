<?php
// Define an array of lessons
$lessons = array(
  array(
    'title' => 'Lesson 1',
    'description' => 'Mathematics Lesson 1 ',
    'category' => 'Math',
    'author' => array(
      'name' => 'Wendy Silvano',
      
    ),
    'image' => '91A73IIT6iL._AC_UF1000,1000_QL80_.jpeg',
    'url' => 'lhttps://www.carsondellosa.com/404103-eb--daily-skill-builders-general-science-resource-book-grade-5-8-ebook-404103-eb/',
  ),
  array(
    'title' => 'Lesson 2',
    'description' => 'This is lesson 2',
    'category' => 'Science',
    'author' => array(
      'name' => 'Jane Doe',
      'image' => 'author2.jpg',
      'profile_url' => 'author2.html',
    ),
    'image' => 'lesson2.jpg',
    'url' => 'lesson2.html',
  ),
  // Add more lessons to the array as needed
);

// Loop through the lessons array and display each lesson
foreach ($lessons as $lesson) {
?>
<div class="card lesson-card">
  <a href="<?php echo $lesson['url']; ?>" class="card-link image w-inline-block">
    <img src="<?php echo $lesson['image']; ?>" alt="<?php echo $lesson['title']; ?>" class="lesson-image" />
  </a>
  <div class="card-data lessons">
    <a href="<?php echo $lesson['category_url']; ?>" class="category-link w-inline-block">
      <div class="category"><?php echo $lesson['category']; ?></div>
    </a>
    <a href="<?php echo $lesson['url']; ?>" class="card-link w-inline-block">
      <h3 class="card-title"><?php echo $lesson['title']; ?></h3>
      <p><?php echo $lesson['description']; ?></p>
    </a>
  </div>
  <a href="<?php echo $lesson['author']['profile_url']; ?>" class="author-info lesson-card w-inline-block">
    <img src="<?php echo $lesson['author']['image']; ?>" alt="<?php echo $lesson['author']['name']; ?>" class="avatar" />
    <div>by</div>
    <div class="author-name"><?php echo $lesson['author']['name']; ?></div>
  </a>
</div>
<?php
}
?>
