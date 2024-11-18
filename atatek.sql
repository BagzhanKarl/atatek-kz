-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Хост: 127.0.0.1:3306
-- Время создания: Ноя 18 2024 г., 11:44
-- Версия сервера: 10.8.4-MariaDB
-- Версия PHP: 7.2.34

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- База данных: `atatek`
--

-- --------------------------------------------------------

--
-- Структура таблицы `pages`
--

CREATE TABLE `pages` (
  `id` int(11) NOT NULL,
  `title` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `juz` varchar(255) COLLATE utf8mb4_unicode_ci NOT NULL,
  `breed1` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `breed2` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `breed3` varchar(255) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `item` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `pages`
--

INSERT INTO `pages` (`id`, `title`, `juz`, `breed1`, `breed2`, `breed3`, `item`) VALUES
(2, 'Жарты', 'Ұлы жүз', 'alban', 'sary', 'zharty', 25);

-- --------------------------------------------------------

--
-- Структура таблицы `places`
--

CREATE TABLE `places` (
  `id` int(11) NOT NULL,
  `osm` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `lat` float NOT NULL,
  `lon` float NOT NULL,
  `type` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `name` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `display_name` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `places`
--

INSERT INTO `places` (`id`, `osm`, `lat`, `lon`, `type`, `name`, `display_name`) VALUES
(1, '38804393', 43.0217, 79.2232, 'town', 'Кеген', 'Кеген, Кеген ауданы, Алматы облысы, 041400, Қазақстан'),
(2, '14475566', 43.0498, 79.7961, 'river', 'Кеген', 'Кеген, Алматы облысы, Қазақстан'),
(3, '1026934664', 42.4045, 69.5385, 'residential', 'Кеген', 'Кеген, Нұршуақ, Абай ауданы, Шымкент, 160020, Қазақстан'),
(4, '9159398', 42.9993, 78.4543, 'administrative', 'Кеген ауданы', 'Кеген ауданы, Алматы облысы, Қазақстан'),
(5, '2465058', 43.2364, 76.9457, 'administrative', 'Алматы', 'Алматы, Қазақстан');

-- --------------------------------------------------------

--
-- Структура таблицы `referrals`
--

CREATE TABLE `referrals` (
  `id` int(11) NOT NULL,
  `referrer_id` int(11) NOT NULL,
  `referred_id` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `referrals`
--

INSERT INTO `referrals` (`id`, `referrer_id`, `referred_id`, `created_at`) VALUES
(2, 2, 3, '2024-11-18 00:43:46'),
(3, 2, 4, '2024-11-18 00:44:29');

-- --------------------------------------------------------

--
-- Структура таблицы `roles`
--

CREATE TABLE `roles` (
  `id` int(11) NOT NULL,
  `title` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `js` varchar(80) COLLATE utf8mb4_unicode_ci NOT NULL,
  `add_child` int(11) NOT NULL,
  `add_info` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `roles`
--

INSERT INTO `roles` (`id`, `title`, `js`, `add_child`, `add_info`) VALUES
(1, 'Бастау', 'bastay.js', 0, 0),
(2, 'Сарапшы', 'sarapshy.js', 10, 10),
(3, 'Алтын', 'altyn.js', 10, 10),
(4, 'Модератор', 'moderator.js', 10, 10),
(5, 'Администратор', 'admin.js', 15000, 15000);

-- --------------------------------------------------------

--
-- Структура таблицы `subscriptions`
--

CREATE TABLE `subscriptions` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `role` int(11) NOT NULL,
  `addchild` int(11) NOT NULL,
  `addinfo` int(11) NOT NULL,
  `start_date` datetime NOT NULL,
  `end_date` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tickets`
--

CREATE TABLE `tickets` (
  `id` int(11) NOT NULL,
  `type` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_cancelled` tinyint(1) NOT NULL,
  `is_completed` tinyint(1) NOT NULL,
  `created_at` datetime NOT NULL,
  `created_by` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `birth` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `death` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `info` text COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tree_id` int(11) DEFAULT NULL,
  `name_new` varchar(50) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `parent` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `transaction`
--

CREATE TABLE `transaction` (
  `id` int(11) NOT NULL,
  `user` int(11) DEFAULT NULL,
  `role` int(11) DEFAULT NULL,
  `childCount` int(11) DEFAULT NULL,
  `infoCount` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `tree`
--

CREATE TABLE `tree` (
  `id` int(11) NOT NULL,
  `item_id` int(11) NOT NULL,
  `name` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `birth_year` int(11) DEFAULT NULL,
  `death_year` int(11) DEFAULT NULL,
  `parent_id` int(11) DEFAULT NULL,
  `juz` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int(11) NOT NULL,
  `updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `tree`
--

INSERT INTO `tree` (`id`, `item_id`, `name`, `birth_year`, `death_year`, `parent_id`, `juz`, `created_at`, `updated_at`, `created_by`, `updated_by`) VALUES
(1, 14, 'Алаш', NULL, NULL, NULL, NULL, '2024-11-17 01:37:31', '2024-11-17 23:33:30', 0, 0),
(2, 1, 'Ұлы жүз', NULL, NULL, 1, NULL, '2024-11-17 02:19:29', '2024-11-17 02:19:29', 0, 0),
(3, 2, 'Орта жүз', NULL, NULL, 1, NULL, '2024-11-17 02:19:29', '2024-11-17 02:19:29', 0, 0),
(4, 3, 'Кіші жүз', NULL, NULL, 1, NULL, '2024-11-17 02:19:29', '2024-11-17 02:19:29', 0, 0),
(5, 4, 'Жүзден тыс', NULL, NULL, 1, NULL, '2024-11-17 02:19:29', '2024-11-17 02:19:29', 0, 0),
(6, 517179, 'Қаңлы', 0, 0, 2, NULL, '2024-11-17 02:20:12', '2024-11-17 02:20:12', 0, 0),
(7, 517180, 'Шанышқылы', 0, 0, 2, NULL, '2024-11-17 02:20:12', '2024-11-17 02:20:12', 0, 0),
(8, 367, 'Жалайыр', 600, 700, 2, NULL, '2024-11-17 02:20:12', '2024-11-17 02:20:12', 0, 0),
(9, 514394, 'Сіргелі', 0, 0, 2, NULL, '2024-11-17 02:20:12', '2024-11-17 02:20:12', 0, 0),
(10, 65602, 'Шақшам', NULL, NULL, 2, NULL, '2024-11-17 02:20:12', '2024-11-17 02:20:12', 0, 0),
(11, 15, 'Сарыүйсін', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(12, 364, 'Шапырашты', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(13, 365, 'Ысты', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(14, 362, 'Ошақты', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(15, 5, 'Албан', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(16, 363, 'Суан', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(17, 6, 'Дулат', 0, 0, 2, NULL, '2024-11-17 02:20:13', '2024-11-17 02:20:13', 0, 0),
(18, 374, 'Сары', NULL, NULL, 15, NULL, '2024-11-17 02:20:30', '2024-11-17 02:20:30', 0, 0),
(19, 375, 'Шыбыл', NULL, NULL, 15, NULL, '2024-11-17 02:20:30', '2024-11-17 02:20:30', 0, 0),
(20, 771, 'Сүйерқұл', NULL, NULL, 18, NULL, '2024-11-17 02:20:32', '2024-11-17 02:20:32', 0, 0),
(21, 772, 'Сүйменді-Таубұзар', NULL, NULL, 18, NULL, '2024-11-17 02:20:32', '2024-11-17 02:20:32', 0, 0),
(22, 618175, 'Шоған', 1584, 1642, 20, NULL, '2024-11-17 02:20:35', '2024-11-17 02:20:35', 0, 0),
(23, 775, 'Досалы', NULL, NULL, 20, NULL, '2024-11-17 02:20:35', '2024-11-17 02:20:35', 0, 0),
(24, 776, 'Қожбанбет', NULL, NULL, 20, NULL, '2024-11-17 02:20:35', '2024-11-17 02:20:35', 0, 0),
(25, 779, 'Жарты-Мұсылманбай', 1542, 1615, 20, NULL, '2024-11-17 02:20:35', '2024-11-17 02:20:35', 0, 0),
(26, 1061, 'Малдыыстық', NULL, NULL, 12, NULL, '2024-11-17 02:26:44', '2024-11-17 02:26:44', 0, 0),
(27, 693644, 'Желдіыстық', NULL, NULL, 12, NULL, '2024-11-17 02:26:44', '2024-11-17 02:26:44', 0, 0),
(28, 910481663, 'Қалдыыстық', NULL, NULL, 12, NULL, '2024-11-17 02:26:44', '2024-11-17 02:26:44', 0, 0),
(29, 910481684, 'Екей', NULL, NULL, 26, NULL, '2024-11-17 02:26:46', '2024-11-17 02:26:46', 0, 0),
(30, 910481685, 'Еміл', NULL, NULL, 26, NULL, '2024-11-17 02:26:46', '2024-11-17 02:26:46', 0, 0),
(33, 0, 'Тест', NULL, NULL, NULL, NULL, '2024-11-17 22:52:47', '2024-11-17 22:58:57', 0, 0),
(34, 0, 'Пест', NULL, NULL, NULL, NULL, '2024-11-17 22:52:47', '2024-11-17 22:58:57', 0, 0),
(35, 0, 'Ест', NULL, NULL, NULL, NULL, '2024-11-17 22:52:47', '2024-11-17 22:58:57', 0, 0),
(36, 7, 'Арғын', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(37, 910588591, 'Найман', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(38, 8, 'Қоңырат', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(39, 371, 'Қыпшақ', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(40, 372, 'Керей', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(41, 373, 'Уақ', 0, 0, 3, NULL, '2024-11-18 00:01:37', '2024-11-18 00:01:37', 0, 0),
(42, 773501, 'Айдабол', NULL, NULL, 25, NULL, '2024-11-18 06:14:00', '2024-11-18 06:14:00', 0, 0),
(43, 773502, 'Жандабол', NULL, NULL, 25, NULL, '2024-11-18 06:14:00', '2024-11-18 06:14:00', 0, 0),
(44, 786822, 'Әзет', NULL, NULL, 42, NULL, '2024-11-18 06:21:23', '2024-11-18 06:21:23', 0, 0),
(45, 786823, 'Нәзет', NULL, NULL, 42, NULL, '2024-11-18 06:21:23', '2024-11-18 06:21:23', 0, 0),
(46, 982107, 'Борық', NULL, NULL, 42, NULL, '2024-11-18 06:21:23', '2024-11-18 06:21:23', 0, 0),
(47, 982108, 'Бөлшек', NULL, NULL, 42, NULL, '2024-11-18 06:21:23', '2024-11-18 06:21:23', 0, 0),
(48, 982109, 'Өстемір', NULL, NULL, 42, NULL, '2024-11-18 06:21:23', '2024-11-18 06:21:23', 0, 0);

-- --------------------------------------------------------

--
-- Структура таблицы `tree_info`
--

CREATE TABLE `tree_info` (
  `id` int(11) NOT NULL,
  `tree_id` int(11) DEFAULT NULL,
  `info` text COLLATE utf8mb4_unicode_ci NOT NULL,
  `tree_icon` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `tree_full_icon` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_by` int(11) NOT NULL,
  `updated_by` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- --------------------------------------------------------

--
-- Структура таблицы `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `phone` varchar(12) COLLATE utf8mb4_unicode_ci NOT NULL,
  `password` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `first_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `last_name` varchar(20) COLLATE utf8mb4_unicode_ci NOT NULL,
  `country` varchar(50) COLLATE utf8mb4_unicode_ci NOT NULL,
  `address` varchar(250) COLLATE utf8mb4_unicode_ci NOT NULL,
  `role` int(11) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `is_verify` tinyint(1) NOT NULL,
  `is_superadmin` tinyint(1) NOT NULL,
  `page` int(11) DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Дамп данных таблицы `users`
--

INSERT INTO `users` (`id`, `phone`, `password`, `first_name`, `last_name`, `country`, `address`, `role`, `is_active`, `is_verify`, `is_superadmin`, `page`, `created_at`, `updated_at`) VALUES
(2, '+77777777777', '$2b$12$xwYB3qSXyV/oucvN546pAORaSczvLcFvsDruE.QUNUVtqv0g.E0t.', 'Алтын', 'Тест', 'Kazakhstan', '2465058', 3, 1, 0, 0, 2, '2024-11-18 00:43:05', '2024-11-18 00:43:05'),
(3, '+77777777771', '$2b$12$KbuBSLDoyTxKQqBkTM1Dbu4RxGBfSTDj8OiTgKAfiY5J5dK.x4KoC', 'Сарапшы', 'Тест', 'Kazakhstan', '2465058', 2, 1, 0, 0, 2, '2024-11-18 00:43:46', '2024-11-18 00:43:46'),
(4, '+77777777772', '$2b$12$ehDmmTQDlGpEi7dMAd/QAexgKe74cSiagxZQgvcFBZPOusQ53spK.', 'Бастау', 'Тест', 'Kazakhstan', '2465058', 1, 1, 0, 0, 2, '2024-11-18 00:44:29', '2024-11-18 00:44:29'),
(5, '+77085904532', '$2b$12$YO4aRkcKrLWn5E4yHBGwXeHCJLRSf7u48NHVl/N177YZumc7MYJb6', 'Бағжан', 'Карл', 'Kazakhstan', '38804393', 5, 1, 0, 0, 2, '2024-11-18 02:51:54', '2024-11-18 02:51:54');

-- --------------------------------------------------------

--
-- Структура таблицы `verify`
--

CREATE TABLE `verify` (
  `id` int(11) NOT NULL,
  `user` int(11) NOT NULL,
  `code` int(11) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `before_time` datetime DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

--
-- Индексы сохранённых таблиц
--

--
-- Индексы таблицы `pages`
--
ALTER TABLE `pages`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ix_pages_item` (`item`),
  ADD KEY `ix_pages_id` (`id`),
  ADD KEY `ix_pages_juz` (`juz`);

--
-- Индексы таблицы `places`
--
ALTER TABLE `places`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `referrals`
--
ALTER TABLE `referrals`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique_referral` (`referrer_id`,`referred_id`),
  ADD KEY `referred_id` (`referred_id`);

--
-- Индексы таблицы `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `title` (`title`),
  ADD UNIQUE KEY `js` (`js`);

--
-- Индексы таблицы `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD PRIMARY KEY (`id`),
  ADD KEY `user` (`user`),
  ADD KEY `role` (`role`);

--
-- Индексы таблицы `tickets`
--
ALTER TABLE `tickets`
  ADD PRIMARY KEY (`id`),
  ADD KEY `created_by` (`created_by`);

--
-- Индексы таблицы `transaction`
--
ALTER TABLE `transaction`
  ADD PRIMARY KEY (`id`);

--
-- Индексы таблицы `tree`
--
ALTER TABLE `tree`
  ADD PRIMARY KEY (`id`),
  ADD KEY `parent_id` (`parent_id`),
  ADD KEY `juz` (`juz`);

--
-- Индексы таблицы `tree_info`
--
ALTER TABLE `tree_info`
  ADD PRIMARY KEY (`id`),
  ADD KEY `tree_id` (`tree_id`);

--
-- Индексы таблицы `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `phone` (`phone`);

--
-- Индексы таблицы `verify`
--
ALTER TABLE `verify`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT для сохранённых таблиц
--

--
-- AUTO_INCREMENT для таблицы `pages`
--
ALTER TABLE `pages`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT для таблицы `places`
--
ALTER TABLE `places`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `referrals`
--
ALTER TABLE `referrals`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT для таблицы `roles`
--
ALTER TABLE `roles`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `subscriptions`
--
ALTER TABLE `subscriptions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `tickets`
--
ALTER TABLE `tickets`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `transaction`
--
ALTER TABLE `transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `tree`
--
ALTER TABLE `tree`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=49;

--
-- AUTO_INCREMENT для таблицы `tree_info`
--
ALTER TABLE `tree_info`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT для таблицы `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT для таблицы `verify`
--
ALTER TABLE `verify`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- Ограничения внешнего ключа сохраненных таблиц
--

--
-- Ограничения внешнего ключа таблицы `referrals`
--
ALTER TABLE `referrals`
  ADD CONSTRAINT `referrals_ibfk_1` FOREIGN KEY (`referrer_id`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `referrals_ibfk_2` FOREIGN KEY (`referred_id`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `subscriptions`
--
ALTER TABLE `subscriptions`
  ADD CONSTRAINT `subscriptions_ibfk_1` FOREIGN KEY (`user`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `subscriptions_ibfk_2` FOREIGN KEY (`role`) REFERENCES `roles` (`id`);

--
-- Ограничения внешнего ключа таблицы `tickets`
--
ALTER TABLE `tickets`
  ADD CONSTRAINT `tickets_ibfk_1` FOREIGN KEY (`created_by`) REFERENCES `users` (`id`);

--
-- Ограничения внешнего ключа таблицы `tree`
--
ALTER TABLE `tree`
  ADD CONSTRAINT `tree_ibfk_1` FOREIGN KEY (`parent_id`) REFERENCES `tree` (`id`),
  ADD CONSTRAINT `tree_ibfk_2` FOREIGN KEY (`juz`) REFERENCES `tree` (`id`);

--
-- Ограничения внешнего ключа таблицы `tree_info`
--
ALTER TABLE `tree_info`
  ADD CONSTRAINT `tree_info_ibfk_1` FOREIGN KEY (`tree_id`) REFERENCES `tree` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
