import 'package:flutter/material.dart';
import 'package:ui/screens/loading.dart';
import 'package:flutter_riverpod/flutter_riverpod.dart';
import 'package:flutter_dotenv/flutter_dotenv.dart';
import 'package:ui/widgets/app_menu_bar.dart';
import 'package:window_manager/window_manager.dart';

Future<void> main() async {
  await dotenv.load(fileName: ".env");

  WidgetsFlutterBinding.ensureInitialized();
  await windowManager.ensureInitialized();

  WindowOptions windowOptions = const WindowOptions(
    titleBarStyle: TitleBarStyle.hidden,
  );

  await windowManager.waitUntilReadyToShow(windowOptions, () async {
    await windowManager.show();
    await windowManager.focus();
  });

  runApp(ProviderScope(child: const MyApp()));
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'DB-Ninja',
      theme: ThemeData(
        brightness: Brightness.dark,
        colorScheme: const ColorScheme.dark(
          primary: Color(0xFF1B5E20),
          secondary: Color(0xFF4CAF50),
          surface: Color(0xFF121212),
        ),
        scaffoldBackgroundColor: const Color(0xFF0A0A0A),
        appBarTheme: const AppBarTheme(
          backgroundColor: Color(0xFF1B5E20),
          foregroundColor: Colors.white,
        ),
        useMaterial3: true,
      ),
      // Remove the builder and put AppMenuBar in home instead
      home: const AppWithMenuBar(),
    );
  }
}

// New wrapper widget
class AppWithMenuBar extends StatefulWidget {
  const AppWithMenuBar({super.key});

  @override
  State<AppWithMenuBar> createState() => _AppWithMenuBarState();
}

class _AppWithMenuBarState extends State<AppWithMenuBar> {
  final GlobalKey<NavigatorState> _navigatorKey = GlobalKey<NavigatorState>();

  @override
  Widget build(BuildContext context) {
    return AppMenuBar(
      navigatorKey: _navigatorKey,
      child: Navigator(
        key: _navigatorKey,
        onGenerateRoute: (settings) {
          return MaterialPageRoute(builder: (context) => const LoadingScreen());
        },
      ),
    );
  }
}
